from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/director/',include('director.urls',namespace='director')),
    path('api/star/',include('star.urls',namespace='star')),
    path('api/movie/',include('movie.urls',namespace='movie')),
    path('api/genre/',include('genre.urls',namespace='genre')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
