from django.contrib import admin
from django.urls import path

from . import views
def DesdeApps(self):
    print('desde persona')

urlpatterns = [
    path('', DesdeApps),
    path('list/', views.UserListApiView.as_view(),),
    path('create/', views.UserCreateView.as_view(),),
    path('detail/<pk>/', views.UserDetailView.as_view(),),
    path('delete/<pk>/', views.UserDeleteView.as_view(),),
    path('update/<pk>/', views.UserUpdateView.as_view(),),
    path('modificar/<pk>/', views.UserRetriveUpdateView.as_view(),),
]