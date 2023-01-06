from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
]
