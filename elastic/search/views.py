from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .models import Biblioteca
from .serializer import DocumentoSerializer
from .documents import BibliotecaDocument
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def SubirDocumento(request):
    """
    Funcion para subir documento en formato formulario html
    {
        "id": "",
        "dispositionTitle": "",
        "date": "",
        "volume": "",
        "pageNumbers": "",
        "legislationTranscriptOriginal": "documentoPDF",
        "legislationTranscriptCopy": "",
        "place": "",
        "dispositionTypeId": "",
        "affairId": "",
    }
    """
    serializer = DocumentoSerializer(data=request.data) # Serializar datos del request
    if serializer.is_valid(): # Se valida la data
        serializer.save() # Se guardan los datos en db y elastic search
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def BuscarDocumento(request):
    """
    Funcion para busqueda de docuemntos en la base de datos en un formulario 
    {
        "search":"<palabra_a_buscar>"
    }
    """
    if request.GET.get('search'):
        search = request.GET.get('search') 
        #------ Query de busqueda en elastic search y se guardan los resultados en response ---------
        s = BibliotecaDocument.search().query("multi_match", query=search,
        fields=['dispositionTitle', 'date', 'volume', 'pageNumbers', 'legislationTranscriptCopy', 'place', 'dispositionTypeId', 'affairId']) 
        response = s.execute()
        #--------------------------------------------------------------------------------------------
        res = DocumentoSerializer(response.hits, many=True) # Deserializacion de resultados de busqueda
        for i in range(0,len(res.data)):
            res.data[i]['legislationTranscriptOriginal'] = response.hits[i]['legislationTranscriptOriginal']

        return Response(res.data, status=status.HTTP_200_OK)
    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)

