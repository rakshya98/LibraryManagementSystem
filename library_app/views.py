from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *

class CreateUserView(generics.CreateAPIView):
    authentication_classes = []  
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListAllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GetUserByIDView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'UserID'

class AddNewBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListAllBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GetBookByIDView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookID'


class AssignUpdateBookDetailsView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'BookID'
    
    def create(self, request, *args, **kwargs):
        book_id = kwargs.get('BookID')
        book_instance = get_object_or_404(Book, BookID=book_id)
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(BookID=book_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

class BorrowBookView(generics.CreateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

    def create(self, request, *args, **kwargs):
       
        user_id = request.data.get('UserID')
        book_id = request.data.get('BookID')

        user = get_object_or_404(User, UserID=user_id)
        book = get_object_or_404(Book, BookID=book_id)
       
        if BorrowedBooks.objects.filter(BookID=book_id).exists():
            return Response({"error": "Book is  currently borrowed."}, status=status.HTTP_400_BAD_REQUEST)
 
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnBookView(generics.UpdateAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
    lookup_field = 'BookID'
    
    def get(self, request, *args, **kwargs):
        borrowed_book = self.get_object()
        serializer = self.get_serializer(borrowed_book)
        return Response(serializer.data)

class ListAllBorrowedBooksView(generics.ListAPIView):
    queryset = BorrowedBooks.objects.filter(ReturnDate=None)
    serializer_class = BorrowedBooksSerializer
