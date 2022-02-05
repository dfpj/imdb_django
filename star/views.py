from .serilizers import StarSerilalizer
from .models import Star
from rest_framework.generics import (CreateAPIView ,RetrieveAPIView,ListAPIView,
DestroyAPIView,UpdateAPIView)
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response

class CreateStarView(CreateAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerilalizer
    permission_classes = [IsAdminUser]

class ListStarView(ListAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerilalizer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class RetrieveStarView(RetrieveAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerilalizer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class UpdateStarView(UpdateAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerilalizer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.partial_update( request, *args, **kwargs)

class DestroyStarView(DestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerilalizer
    permission_classes = [IsAdminUser]

class ListStarIncompleteView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request, *args, **kwargs):
        stars= Star.objects.filter(name__isnull=True)
        serializer = StarSerilalizer(stars,many=True)
        return Response(serializer.data)