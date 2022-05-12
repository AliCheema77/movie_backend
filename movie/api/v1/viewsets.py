from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie, Comment
from rest_framework.viewsets import ModelViewSet
from movie.api.v1.serializers import MovieSerializer, MovieTitleSerializer, CommentSerializer
import requests
from requests.auth import HTTPBasicAuth
from rest_framework.views import APIView
from django.conf import settings

API_KEY = settings.API_KEY


class PostMovieView(APIView):
    serializer_class = MovieTitleSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            url = 'http://www.omdbapi.com/?'
            api_key = API_KEY
            title = data.get("title")
            res = requests.get(f'{url}t={title}&apikey={api_key}')
            if res.status_code == 200:
                data = res.json()
                movie = Movie(title=data.get("Title"), year=data.get("year"), rated=data.get("Rated"),
                              released=data.get("Released"), runtime=data.get("Runtime"), genre=data.get("Genre"),
                              director=data.get("Director"), writer=data.get("Writer"), actors=data.get("Actors"),
                              plot=data.get("Plot"), language=data.get("language"), country=data.get("Country"),
                              awards=data.get("Awards"), poster=data.get("Poster"))
                movie.save()
                title = movie.title
                new_obj = Movie.objects.get(title__exact=title)
                seria = MovieSerializer(new_obj, many=False)
                return Response({"response": seria.data}, status=status.HTTP_200_OK)
            return Response({"response": res}, status=status.HTTP_400_BAD_REQUEST)


class FetchAllMovies(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ['get']


class PostCommentView(APIView):
    serializer_class = CommentSerializer

    def get(self, request):
        comments = Comment.objects.all()
        serializer = self.serializer_class(comments, many=True)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'response': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"response": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class FetchCommentView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, movie_id):
        if movie_id:
            comments = Comment.objects.filter(movie_id=movie_id)
        else:
            comments = Comment.objects.all()
        serializer = self.serializer_class(comments, many=True)
        return Response({"response": serializer.data}, status=status.HTTP_200_OK)



