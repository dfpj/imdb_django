from rest_framework import serializers
from .models import Genre

class GenreSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields =('title',)