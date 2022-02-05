from rest_framework import serializers
from .models import Movie
from star.models import Star
from director.models import Director
from genre.models import Genre
from genre.serilizers import GenreSerilalizer
from star.serilizers import StarSerilalizer
from director.serilizers import DirectorSerilalizer


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerilalizer(Genre.objects.all(), many=True).data
    stars = StarSerilalizer(Star.objects.all(), many=True).data
    directors = DirectorSerilalizer(Director.objects.all(), many=True).data

    class Meta:
        model = Movie
        fields = ('slug', 'title', 'published', 'duration', 'votes', 'summary',
                  'rate', 'gross', 'score', 'image', 'genres', 'directors', 'stars')
