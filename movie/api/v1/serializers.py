from rest_framework import serializers
from movie.models import Movie, Comment


class MovieTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["movie"] = instance.movie.title
        return data
