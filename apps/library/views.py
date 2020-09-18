from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from apps.library.models import Genre, Book
from apps.library.serializers import GenreSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status

# GenreViewSet class inherits from ModelViewSet to use inherited CRUD functions (including partial_update)
class GenreViewSet(viewsets.ModelViewSet):
    # You must be logged in to view genres
    permission_classes = (IsAuthenticated,)

    # serializing output and deserializing data input:
    serializer_class = GenreSerializer

    # Override generic queryset (basename provided in the URL router)
    def get_queryset(self):
        # Return all genres that belong to the user
        query_set = Genre.objects.all().filter(user=self.request.user)
        return query_set

    # Override .create():
    def create(self, request, *args, **kwargs):
        # Get the genre by name and belongs to the user
        genre = Genre.objects.filter(
            user=self.request.user,
            name=request.data.get('name')
        )
        # If there is such genre for that user, then error is raised to prevent user from recreating the same genre
        if genre:
            raise ValidationError("This genre exists already.")

        # If there is no such genre for that user, then deserialize incoming request data in the body before creating
        serializer = GenreSerializer(data=request.data)
        # If serializer finds the incoming request data matching itself, then it is valid and will create the genre object by taking in request
        if serializer.is_valid():
            return super().create(request)

    def perform_create(self, serializer):
        # Return the created object by calling .save() during the deserialization
        serializer.save(user=self.request.user) # add additional data not part of the request data, like the current user to the genre object

    def destroy(self, request, *args, **kwargs):
        # print(kwargs)
        genre = Genre.objects.get(pk=self.kwargs['pk'])
        if not self.request.user == genre.user:
            raise PermissionDenied("You are not authorized to delete the genre")
        super().destroy(request, *args, **kwargs)
        return Response({
            "message": "You successfully deleted the genre"
        })

# Inherit from ListCreate APIView to get a list of all books in a genre and create book in a genre
class AllBooks(generics.ListCreateAPIView):
    # User can only see all books in a genre and create book in a genre if logged in
    permission_classes = (IsAuthenticated,)

    # serializing output and deserializing data input:
    serializer_class = BookSerializer

    # Override get_queryset() view method to check if user has the book under the genre
    def get_queryset(self):
        # Try and except block to see if user enters a genre_pk in url that user does not have (either genre_pk is not in the db or belongs to another user). If user enters a genre_pk for the genre id that user does not have that the except runs
        try:
            # If a genre_pk is provided in the URL, get that genre and then the books in the genre:
            if self.kwargs.get('genre_pk'):
                # Will raise the except code when genre_pk belongs to another user:
                one_genre = Genre.objects.get(
                    pk=self.kwargs.get('genre_pk'),
                    user=self.request.user
                )
                # Get all books under the genre from the user:
                books = Book.objects.filter(
                    user=self.request.user,
                    genre=one_genre
                )
                # If there are no books yet under the genre, then raise an error, else return all books under the genre of that user
                if not books:
                    raise ValidationError("You have not made a book yet in this genre")
                else:
                    return books
        except Genre.DoesNotExist:
            raise ValidationError("You cannot access to books in the genre that you do not have") # pass does not work here

    # Override the inherited create method to customize error
    def create(self, request, *args, **kwargs):
        # Grab the genre value from the incoming request data and check if the user has that genre by grabbing that genre in the if statement. If user does have the genre, then the user can create books under that genre. If the genre does not exist or belongs to another user, then the Validation Error is raised.
        try:
            if self.request.user.genres.get(pk=self.request.data['genre']):
                # If data is valid during deserialization, then create book object
                return super().create(request)
        except Genre.DoesNotExist:
            raise ValidationError("You cannot create the book in a genre that you do not have access to")

    def perform_create(self, serializer):
        # Return the created book object with additional info to the book object
        serializer.save(user=self.request.user)


class SingleBook(generics.RetrieveUpdateDestroyAPIView):
    # User can only see, update, and delete one book in a genre if logged in
    permission_classes = (IsAuthenticated,)

    # Serializing output and deserializing data input:
    serializer_class = BookSerializer

    # Override get_queryset() method in order to check if user has the book under the genre:
    def get_queryset(self):
        # If the URL provides the id of genre and id of book, then get the genre. If the genre does not exist in the db or if the genre belongs to someone else then unable to return the books in the genre, the except code block is run.
        try:
            if self.kwargs.get('genre_pk') and self.kwargs.get('pk'):
                genre = Genre.objects.get(pk=self.kwargs['genre_pk'])
                return Book.objects.filter(
                    user=self.request.user,
                    pk=self.kwargs['pk'],
                    genre=genre
                )
        except Genre.DoesNotExist:
            pass

    def update(self, request, *args, **kwargs):
        # Check to see if the user has the genre provided in request data by grabbing the genre under that user. If user does not have the genre provided from the request data, either the genre does not exist in the db or belongs to someone else, then Validation Error is run, regardless if the URL has the ids of the book and genre that belongs to the user or does not belongs to the user.
        try:
            if self.request.user.genres.get(pk=self.request.data['genre']):
                return super().update(request, *args, **kwargs)
        except Genre.DoesNotExist:
            raise ValidationError("You cannot update the book in a genre that you do not have access to")

    def destroy(self, request, *args, **kwargs):
        # Try to see if the user has the genre provided in the URL. If user does not have the genre provided from the URL, either the genre does not exist in db or belongs to someone else, then the except block is run.
        try:
            if self.request.user.genres.get(pk=self.kwargs['genre_pk']):
                super().destroy(request, *args, **kwargs)
                return Response({
                    "message": "Successfully deleted"
                })
        except Genre.DoesNotExist:
            raise ValidationError("You cannot delete the book in a genre that you do not have access to")









