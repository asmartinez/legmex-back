from django.urls import path

from .views import ListTpe_col_cattdisp

urlpatterns = [
    path('dispositions/',ListTpe_col_cattdisp.as_view(), name='lista-Dispositions' ),
]