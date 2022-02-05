from .serilizers import DirectorSerilalizer
from .models import Director
from rest_framework.generics import (CreateAPIView ,RetrieveAPIView,ListAPIView,
DestroyAPIView,UpdateAPIView)
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CreateDirectorView(CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer
    permission_classes = [IsAdminUser]

class ListDirectorView(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class RetrieveDirectorView(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class UpdateDirectorView(UpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.partial_update( request, *args, **kwargs)

class DestroyDirectorView(DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerilalizer
    permission_classes = [IsAdminUser]