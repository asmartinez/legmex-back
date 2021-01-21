from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Affair
from .serializers import AffairSerializer

# Create your views here.
class ListAffair(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        asuntos = Affair.objects.all()
        asuntos_json = AffairSerializer(asuntos, many = True)
        return Response(asuntos_json.data) 

    def post(self, request):
        asuntos_json = AffairSerializer(data=request.data)
        if asuntos_json.is_valid():
            asuntos_json.save()
            return Response(asuntos_json.data, status=201)
        return Response(asuntos_json.errors, status=400)
