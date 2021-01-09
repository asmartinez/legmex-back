from django.urls import path
from .views import PersonList

urlpatterns = [
    path('persona/', PersonList.as_view(),name = 'Persona_list'),
]