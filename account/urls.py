# urls.py
from django.conf.urls import url
from django.urls import path#, include
from .api import register_api

urlpatterns = [
	path('api/register/', register_api.as_view(), name='Register')
]