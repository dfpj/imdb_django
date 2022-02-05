from django.urls import path
from .views import CreateMovieView,ListMovieView,RetrieveMovieView,UpdateMovieView,DestroyMovieView

app_name= 'movie'

urlpatterns = [
    path('create/', CreateMovieView.as_view()),
    path('list/', ListMovieView.as_view()),
    path('get/<int:pk>/', RetrieveMovieView.as_view()),
    path('update/<int:pk>/', UpdateMovieView.as_view()),
    path('delete/<int:pk>/', DestroyMovieView.as_view()),
]
