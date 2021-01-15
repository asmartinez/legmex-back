from rest_framework import serializers
from .models import Biblioteca, PDF

#Seralizer de los documentos enviados a elastic search y convertirlos a json
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = ['nombre', 'autor', 'texto', 'archivo']

class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=50)

    