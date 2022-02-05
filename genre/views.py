from .serilizers import GenreSerilalizer
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView,
                                     DestroyAPIView, UpdateAPIView)
from .models import Genre
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

class CreateGenreView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer
    permission_classes = [IsAdminUser]


class RetrieveGenreView(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ListGenreView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer
    permission_classes = [IsAuthenticated]

    # @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class DestroyGenreView(DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerilalizer
    permission_classes = [IsAdminUser]


