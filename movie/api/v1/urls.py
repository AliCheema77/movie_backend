from django.urls import path, include
from movie.api.v1.viewsets import PostMovieView, FetchAllMovies, PostCommentView, FetchCommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("fetch_movies", FetchAllMovies, basename='fetch_movies')

urlpatterns = [
    path('post_movies/', PostMovieView.as_view(), name="post_movies"),
    path('post_comment/', PostCommentView.as_view(), name="post_comment"),
    path('fetch_comment/<int:movie_id>/', FetchCommentView.as_view(), name="fetch_comment"),
    path('', include(router.urls))
]
