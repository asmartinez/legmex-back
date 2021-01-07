# urls.py
from django.conf.urls import url
from django.urls import path#, include
from rest_framework_simplejwt import views as views_jwt
from .api import register_api

urlpatterns = [
	path('api/register/', register_api.as_view(), name='Register'),
    # with views_jwt:
    path('api/token/', views_jwt.TokenObtainPairView.as_view(), name='Token_obtain_pair'),
    path('api/token/refresh/', views_jwt.TokenRefreshView.as_view(), name='Token_refresh'),
]