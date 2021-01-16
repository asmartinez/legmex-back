from rest_framework import serializers
from .models import Biblioteca

#Seralizer de los documentos enviados a elastic search y convertirlos a json
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = "__all__"

class SearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=50)

    