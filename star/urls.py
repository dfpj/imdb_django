from django.urls import path
from .views import CreateStarView
from .views import (CreateStarView,ListStarView,RetrieveStarView,
UpdateStarView,DestroyStarView,ListStarIncompleteView)

app_name= 'star'
urlpatterns = [
    path('create/', CreateStarView.as_view()),
    path('list/', ListStarView.as_view()),
    path('incomplete/', ListStarIncompleteView.as_view()),
    path('get/<str:pk>/', RetrieveStarView.as_view()),
    path('update/<str:pk>/', UpdateStarView.as_view()),
    path('delete/<str:pk>/', DestroyStarView.as_view()),
]

