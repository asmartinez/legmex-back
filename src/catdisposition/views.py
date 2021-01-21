from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Tpe_col_cattdisp
from .serializers import Tpe_col_cattdispSerializer

# Create your views here.
class ListTpe_col_cattdisp(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        disposiciones = Tpe_col_cattdisp.objects.all()
        disposiciones_json = Tpe_col_cattdispSerializer(disposiciones, many = True)
        return Response(disposiciones_json.data) 

    def post(self, request):
        permission_classes = (AllowAny,)
        disposiciones_json = Tpe_col_cattdispSerializer(data=request.data)
        if disposiciones_json.is_valid():
            disposiciones_json.save()
            return Response(disposiciones_json.data, status=201)
        return Response(disposiciones_json.errors, status=400)
