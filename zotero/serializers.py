# serializers.py

from rest_framework import serializers
from .models import zotero_model

class zotero_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = zotero_model
		fields = ('id', 'name', 'title', 'pages')