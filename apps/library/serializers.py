from rest_framework import serializers
from .models import Genre, Book

class BookSerializer(serializers.ModelSerializer):
    # Need to serialize user since we need to deserialize request.user
    user = serializers.ReadOnlyField(source='user.username') # WHAT IS SOURCE FOR? WHAT IS READONLYFIELD FOR? WHY DON'T WE USE READONLYFIELD FOR THE OTHER FIELDS
    # ReadOnlyField: returns the value of the field without modification

    class Meta:
        model = Book
        fields = ('id', 'user', 'genre', 'title', 'author', 'status', 'review', 'created_at', 'updated_at', 'is_public')


class GenreSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    books = BookSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Genre
        fields = ('id', 'user', 'books', 'name', 'created_at', 'updated_at', 'is_public')