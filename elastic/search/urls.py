from django.urls import path
from . import views

urlpatterns = [
    path('document/', views.BuscarDocumento), # URL para busqueda de documento
    path('upload/', views.SubirDocumento), # URL para subir un documento 
    path('document/<int:id>/', views.ModificarDocumento.as_view()),
]
