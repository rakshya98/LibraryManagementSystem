from rest_framework import serializers
from .models import *  
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

        
class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'
    
class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['UserID', 'BookID', 'BorrowDate', 'ReturnDate']
        read_only_fields = ['UserID', 'BookID', 'BorrowDate']
