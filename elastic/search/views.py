from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Biblioteca, PDF
from .serializer import DocumentoSerializer, SearchSerializer, PDFSerializer
from .documents import BibliotecaDocument
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def SubirDocumento(request):
    """
    Funcion para subir documento en el formato json
    {
        "nombre":"<nombre_documento>",
        "autor":"<autor_documetno>",
        "texto":"<texto_documento>",
        "archivo:"<archivo a subir>"
    }
    """
    serializer = DocumentoSerializer(data=request.data) # Serializar datos del request
    if serializer.is_valid(): # Se valida la data
        serializer.save() # Se guardan los datos en db y elastic search
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@parser_classes([JSONParser])
def BuscarDocumento(request):
    """
    Funcion para busqueda de docuemntos en la base de datosen formato json
    {
        "search":"<palabra_a_buscar>"
    }
    """
    serializer = SearchSerializer(data=request.data) # Serializar datos del request
    if serializer.is_valid(): # Se valida la data
        #------ Query de busqueda en elastic search y se guardan los resultados en response ---------
        s = BibliotecaDocument.search().query("multi_match", query=serializer.data['search'], fields=['nombre', 'autor', 'texto']) 
        response = s.execute()
        #--------------------------------------------------------------------------------------------
        res = DocumentoSerializer(response.hits, many=True) # Deserializacion de resultados de busqueda
        return Response(res.data, status=status.HTTP_302_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

