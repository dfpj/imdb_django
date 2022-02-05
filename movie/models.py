from django.db import models
from star.models import Star
from genre.models import Genre
from director.models import Director

class Movie(models.Model):
    slug = models.CharField(unique=True,max_length=50)
    title = models.CharField(max_length=200)
    published = models.CharField(max_length=10)
    duration = models.PositiveSmallIntegerField()
    votes = models.PositiveIntegerField()
    summary = models.TextField()
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    gross = models.DecimalField(max_digits=6, decimal_places=2)
    score = models.PositiveSmallIntegerField(null=True)
    stars = models.ManyToManyField(Star, related_name='movies')
    directors = models.ManyToManyField(Director, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title


