from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Registro

# Create your views here.
class ListRegistro(APIView):
    def get(self, request):
        registros = Registro.objects.all()
        return Response(registros) 