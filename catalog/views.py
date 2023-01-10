from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from django.contrib.auth.decorators import login_required, permission_required
import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import RenewBookForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


@login_required
def books(request):
    """View function for books list page of site."""

    books = Book.objects.all()
    context = {
        'book_list': books,
    }

    return render(request, 'book_list.html', context=context)


@login_required
def book_detail(request, pk):
    """View function for book detail page of site."""
    book = Book.objects.get(id=pk)
    context = {
        'book': book,
    }

    return render(request, 'book_detail.html', context=context)


@login_required
def authors(request):
    """View function for authors list page of site."""

    authors = Author.objects.all()
    context = {
        'author_list': authors,
    }

    return render(request, 'author_list.html', context=context)


@login_required
def author_detail(request, pk):
    """View function for author detail page of site."""
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=pk)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author_detail.html', context=context)


@permission_required('catalog.can_mark_returned', raise_exception=True)
@login_required
def my_books(request):
    """View function for my books page of site."""
    bookinstance_list = BookInstance.objects.filter(
        borrower=request.user).filter(status__exact='o').order_by('due_back')

    context = {
        'bookinstance_list': bookinstance_list
    }

    return render(request, 'my_books.html', context=context)


@permission_required('user.is_staff', raise_exception=True)
@login_required
def all_borrowed(request):
    """View function for all borrowed books page of site"""
    borrowed_books = BookInstance.objects.filter(status='o')

    context = {
        'borrowed_books': borrowed_books
    }
    return render(request, 'borrowed.html', context=context)


@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'book_renew_librarian.html', context)