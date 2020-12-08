from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Biblioteca
from .serializer import DocumentoSerializer, SearchSerializer
from .documents import BibliotecaDocument

# Create your views here.
@api_view(['POST'])
def subir_documento(request):
    """
    Funcion para subir documento en el formato json
    {
        "nombre":"<nombre_documento>",
        "autor":"<autor_documetno>",
        "texto":"<texto_documento>",
    }
    """
    serializer = DocumentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def buscar_documento(request):
    """
    Funcion para busqueda de docuemntos en la base de datosen formato json
    {
        "search":"<palabra_a_buscar>"
    }
    """
    serializer = SearchSerializer(data=request.data)
    if serializer.is_valid():
        s = BibliotecaDocument.search().query("multi_match", query=serializer.data['search'], fields=['nombre', 'autor', 'texto'])
        response = s.execute()
        res = DocumentoSerializer(response.hits, many=True)
        return Response(res.data, status=status.HTTP_302_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
