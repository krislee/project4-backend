from django.db import models
from apps.authorization.models import User

# Create your models here.

class Genre(models.Model):
    # Genre belongs to User
    # User has many genres

    # Add related_name to reference to genre later
    user = models.ForeignKey(User, related_name="genres", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Since is_public is default, is_public is not a required field for request
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower().title()
        return super(Genre, self).save(*args, **kwargs)


class Book(models.Model):
    # Book belongs to genre and user through genre
    # User has many books through genre
    # Genre has many books

    # Add related_name to reference to books later
    user = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name="books", on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.IntegerField(default=2)
    review = models.TextField(blank=True)
    photo = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.lower().title()
        self.author = self.author.lower().title()
        return super(Book, self).save(*args, **kwargs)
