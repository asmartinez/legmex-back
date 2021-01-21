from django.urls import path

from .views import ListAffair

urlpatterns = [
    path('affair/',ListTpe_col_cattdisp.as_view(), name='lista-affair' ),
]