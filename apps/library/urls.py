from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from apps.library.views import GenreViewSet, AllBooks, SingleBook

router = routers.DefaultRouter()

router.register(r'genres', GenreViewSet, basename='genres')

custom_url_patterns = [
    url(r'genres/(?P<genre_pk>\d+)/books$', AllBooks.as_view(), name="genre_books"),
    url(r'genres/(?P<genre_pk>\d+)/books/(?P<pk>\d+)$', SingleBook.as_view(), name="genre_single_book")
]

urlpatterns = router.urls + custom_url_patterns
