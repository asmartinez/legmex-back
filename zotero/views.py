from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import zotero_serializer
from .models import zotero_model
#from zotero.forms import get_tag_formset

class zotero_viewset(viewsets.ModelViewSet):
	queryset = zotero_model.objects.all().order_by('title')
	serializer_class = zotero_serializer

"""
def view_zotero_test(request):
	tag_formset = get_tag_formset(
			obj = form.instance,
			data = request.POST,
			show_labels = False,
			labels = {
				'item_type': 'Document type'
			}
		)
	tag_formset.save()
"""