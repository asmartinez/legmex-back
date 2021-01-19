from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Registro
from .serializers import RegistroSerializer

# Create your views here.
class ListRegistro(APIView):
    def get(self, request):
        registros = Registro.objects.all()
        registro_json = RegistroSerializer(registros, many = True)
        return Response(registro_json.data) 