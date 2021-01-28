from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Tpe_col_cattdisp
from .serializer import Tpe_col_cattdispSerializer

# Create your views here.
def prueba(request):
    return HttpResponse("Primer vista creada")


class Tpe_col_cattdispViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tpe_col_cattdisp.objects.all().order_by('id')
    serializer_class = Tpe_col_cattdispSerializer