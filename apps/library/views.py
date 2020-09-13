from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from apps.library.models import Genre, Book
from apps.library.serializers import GenreSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status

class GenreViewSet(viewsets.ModelViewSet):
    # You must be logged in to view genres
    permission_classes = (IsAuthenticated,)

    # Need a serializer to convert data back and forth
    serializer_class = GenreSerializer

    def get_queryset(self):
        query_set = Genre.objects.all().filter(user=self.request.user)
        return query_set

    def create(self, request, *args, **kwargs):
        genre = Genre.objects.filter(
            user=self.request.user,
            name=request.data.get('name')
        )
        if genre:
            raise ValidationError("This genre exists already.")

        # Serialize incoming request before creating
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            return super().create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# we need to get all books from 1 category
# get one book from 1 category
# create one book in 1 category
# update and delete one book in 1 category

class AllBooks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            if self.kwargs.get('genre_pk'):
                one_genre = Genre.objects.get(
                    pk=self.kwargs.get('genre_pk'),
                    user=self.request.user # can only grab books under the genre that belongs the user else exception is raised
                )
                books = Book.objects.filter(
                    user=self.request.user,
                    genre=one_genre
                )
                if not books:
                    # note: change type of error later
                    raise ValidationError("You cannot access to books in the genre that you do not have")
                else:
                    return books
        except Genre.DoesNotExist:
            # note: change type of error later
            raise ValidationError("You cannot access to books in the genre that you do not have!") # pass does not work here

    def create(self, request, *args, **kwargs):
        try:
            if self.request.user.genres.get(pk=self.request.data['genre']):
                return super().create(request)
        except Genre.DoesNotExist:
            raise ValidationError("You cannot create the book in a genre that you do not have access to")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SingleBook(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
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
        try:
            if self.request.user.genres.get(pk=self.request.data['genre']):
                return super().update(request, *args, **kwargs)
        except Genre.DoesNotExist:
            raise ValidationError("You cannot update the book in a genre that you do not have access to")

    def destroy(self, request, *args, **kwargs):
        try:
            if self.request.user.genres.get(pk=self.kwargs['genre_pk']):
                return super().destroy(request, *args, **kwargs)
        except Genre.DoesNotExist:
            raise ValidationError("You cannot delete the book in a genre that you do not have access to")












