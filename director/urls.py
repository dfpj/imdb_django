from django.urls import path
from .views import CreateDirectorView
from .views import CreateDirectorView,ListDirectorView,RetrieveDirectorView,UpdateDirectorView,DestroyDirectorView

app_name= 'director'

urlpatterns = [
    path('create/', CreateDirectorView.as_view()),
    path('list/', ListDirectorView.as_view()),
    path('get/<str:pk>/', RetrieveDirectorView.as_view()),
    path('update/<str:pk>/', UpdateDirectorView.as_view()),
    path('delete/<str:pk>/', DestroyDirectorView.as_view()),
]
