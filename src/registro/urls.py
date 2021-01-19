from django.urls import path

from .views import ListRegistro

urlpatterns = [
    path('registros/',ListRegistro.as_view(), name='lista-registro' ),
]
