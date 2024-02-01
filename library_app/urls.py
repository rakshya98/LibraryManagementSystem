from django.urls import path
from .views import *

urlpatterns = [
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('users/list/', ListAllUsersView.as_view(), name='list-users'),
    path('users/<int:UserID>/', GetUserByIDView.as_view(), name='get-user-by-id'),
    path('books/add/', AddNewBookView.as_view(), name='add-book'),
    path('books/list/', ListAllBooksView.as_view(), name='list-books'),
    path('books/<int:BookID>/', GetBookByIDView.as_view(), name='get-book-by-id'),
    path('books/<int:BookID>/details/', AssignUpdateBookDetailsView.as_view(), name='assign_update_book_details'),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:BookID>/', ReturnBookView.as_view(), name='return-book'),
    path('list/borrowed/', ListAllBorrowedBooksView.as_view(), name='list-borrowed-books'),
]
