# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

# enrutamiento automático
router = routers.DefaultRouter()
router.register(r'zotero', views.zotero_viewset)

urlpatterns = [
	path('router/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', 'namespaces=rest_framework'))
]