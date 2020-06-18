from django.urls import path
from marvelapi.views import show_films, local_comic_names

urlpatterns = [
    path('MarvelAPI/', show_films, name='show_films'),
    path('MarvelAPIrus/', local_comic_names, name='local_comic_names')
]