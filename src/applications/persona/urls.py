from django.contrib import admin
from django.urls import path

from . import views
def DesdeApps(self):
    print('desde persona')

urlpatterns = [
    path('persona/', DesdeApps),
    path('api/persona/list', views.UserListApiView.as_view(),),
    path('api/persona/create', views.UserCreateView.as_view(),),
]