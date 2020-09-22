from rest_framework import serializers
from .models import Genre, Book

class BookSerializer(serializers.ModelSerializer):
    # Need to serialize user since we need to deserialize the user object (request.user) in view
    user = serializers.ReadOnlyField(source='user.username')
 
    # ReadOnlyField: returns the value of the field without modification
    # ReadOnlyField vs. read_only=True

    class Meta:
        model = Book
        fields = ('id', 'user', 'genre', 'title', 'author', 'status', 'review', 'created_at', 'updated_at', 'is_public', 'photo')


class GenreSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    # When we call on genres list view, books will be a part of each genre, so we need to serialize the books too by calling on Book Serializer
    books = BookSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Genre
        fields = ('id', 'user', 'books', 'name', 'created_at', 'updated_at', 'is_public')