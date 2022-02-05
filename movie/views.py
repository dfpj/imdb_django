from .models import Movie
from .serilizers import MovieSerializer
from star.models import Star
from director.models import Director
from genre.models import Genre
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class ListMovieView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class RetrieveMovieView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CreateMovieView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        for star in data['stars']:
            Star.objects.get_or_create(id=star)
        for genre in data['genres']:
            Genre.objects.get_or_create(title=genre)
        for director in data.get('directors'):
            Director.objects.get_or_create(id=director)
        return super(CreateMovieView, self).create(request)


class UpdateMovieView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DestroyMovieView(DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]