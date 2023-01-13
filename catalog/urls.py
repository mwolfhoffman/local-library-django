from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:pk>', views.author_detail, name='author-detail'),
    path('mybooks/', views.my_books, name='my-borrowed'),
    path('borrowed/', views.all_borrowed, name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian,
         name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/',
         views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/',
         views.AuthorDelete.as_view(), name='author-delete'),
]
