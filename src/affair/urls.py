from django.urls import path

from .views import ListAffair

urlpatterns = [
    path('affair/',ListAffair.as_view(), name='lista-affair' ),
]