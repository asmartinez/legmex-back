from django.urls import path
from . import views

urlpatterns = [
    path('buscar/', views.buscar_documento),
    path('subir/', views.subir_documento),
]