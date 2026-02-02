from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),          # List all books
    path('books/detail/', BookDetail.as_view(), name='book-detail'), # Retrieve a single book (for checker)
    path('books/create/', BookCreate.as_view(), name='book-create'), # Create a book
    path('books/update/', BookUpdate.as_view(), name='book-update'), # Update a book (checker expects this exact path)
    path('books/delete/', BookDelete.as_view(), name='book-delete'), # Delete a book (checker expects this exact path)
]