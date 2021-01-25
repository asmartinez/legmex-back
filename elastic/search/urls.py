from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.BuscarDocumento), # URL para busqueda de documento
    path('upload/', views.SubirDocumento), # URL para subir un documento 
]
