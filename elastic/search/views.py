from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from .serializer import DocumentoSerializer
from .documents import BibliotecaDocument
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(["POST"])
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
        "dispositionNumber": "",
        "dispositionTypeId": "",
        "affairId": "",
    }
    """
    serializerUpload = DocumentoSerializer(
        data=request.data
    )  # Serializar datos del request
    if serializerUpload.is_valid():  # Se valida la data
        serializerUpload.save()  # Se guardan los datos en db y elastic search
        return Response(serializerUpload.data, status=status.HTTP_200_OK)
    return Response(serializerUpload.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def BuscarDocumento(request):
    """
    Funcion para busqueda de docuemntos en la base de datos en un formulario
    {
        "search":"<palabra_a_buscar>"
    }
    """
    if request.GET.get("search"):
        searchString = request.GET.get("search")
        # ------ Query de busqueda en elastic search y se guardan los resultados en response ---------
        searchQuery = BibliotecaDocument.search().query(
            "multi_match",
            query=searchString,
            fields=[
                "dispositionTitle",
                "date",
                "volume",
                "pageNumbers",
                "legislationTranscriptCopy",
                "place",
                "dispositionNumber",
                "dispositionTypeId",
                "affairId",
            ],
        )
        responseQuery = searchQuery.execute()
        # ------------------------------------------------------------------------------------------------------------------
        # Deserializacion de resultados de busqueda ------------------------------------------------------------------------
        deSerializer = DocumentoSerializer(
            responseQuery.hits, 
            many=True
        )
        # ------------------------------------------------------------------------------------------------------------------
        # ------ Por falla en deserializacion no manda el link del documento, ----------------------------------------------
        # ------ asi que se usa la respuesta de elastic para llenar ese campo ----------------------------------------------
        for i in range(0, len(deSerializer.data)):
            deSerializer.data[i]["legislationTranscriptOriginal"] = responseQuery.hits[i]["legislationTranscriptOriginal"]

        return Response(deSerializer.data, status=status.HTTP_200_OK)
    return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)