from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter



from . import views
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

def DesdeApps(self):
    print('desde persona')

urlpatterns = [
    path('persona/', DesdeApps),
    path('api/persona/list', views.UserListApiView.as_view(),),
    path('api/persona/create', views.UserCreateView.as_view(),),
    path('api/persona/detail/<pk>', views.UserDetailView.as_view(),),
    path('api/persona/delete/<pk>', views.UserDeleteView.as_view(),),
    path('api/persona/update/<pk>', views.UserUpdateView.as_view(),),
    path('api/persona/modificar/<pk>', views.UserRetriveUpdateView.as_view(),),
    path('', include(router.urls)),
]