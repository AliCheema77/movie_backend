from django.contrib import admin
from movie.models import Movie, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'rated', 'released', 'runtime', 'genre', 'director', 'writer', 'actors', 'plot',
                    'language', 'country', 'awards', 'poster']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['movie', 'text']
