from django.urls import path
from .views import CreateGenreView,ListGenreView,RetrieveGenreView,DestroyGenreView

app_name= 'genre'

urlpatterns = [
    path('create/', CreateGenreView.as_view()),
    path('list/', ListGenreView.as_view()),
    path('get/<str:pk>/', RetrieveGenreView.as_view()),
    path('delete/<str:pk>/', DestroyGenreView.as_view()),
]
