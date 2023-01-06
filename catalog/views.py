from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre


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


def books(request):
    """View function for books list page of site."""

    books = Book.objects.all()
    context = {
        'book_list': books,
    }

    return render(request, 'book_list.html', context=context)


def book_detail(request, pk):
    """View function for book detail page of site."""
    book = Book.objects.get(id=pk)
    context = {
        'book': book,
    }

    return render(request, 'book_detail.html', context=context)


def authors(request):
    """View function for authors list page of site."""

    authors = Author.objects.all()
    context = {
        'author_list': authors,
    }

    return render(request, 'author_list.html', context=context)


def author_detail(request, pk):
    """View function for author detail page of site."""
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=pk)
    context = {
        'author': author,
        'books': books
    }
    return render(request, 'author_detail.html', context=context)
