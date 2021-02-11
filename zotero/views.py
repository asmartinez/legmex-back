from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
#from .serializers import zotero_serializer
#from .models import zotero_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from pyzotero import zotero


# ----------ZOTERO (pyzotero)
# library_id=user-id(for api calls),
# library_type=user/group,
# api_key *for this case, this is full-admin)
zotero = zotero.Zotero('7483577', 'user', 'atfoGmMcFlqnSNQ4BmAT3tPa')
zot = zotero.everything(zotero.top())
# we can print each item's item type and ID ---------------------

# ---------------------------------------------- Read API Methods - return:
# ------------------------------ Retrieving Items:
@api_view(["GET"])
def key_info_view(request):  # dict
	return Response(zotero.key_info())

@api_view(["GET"])  ### ([search/request parameters])
def items_view(request):  # list of dicts
	return Response(zotero.items())

@api_view(["GET"])
def count_items_view(request):  # int
	return Response(zotero.count_items())

@api_view(["GET"])  ### ([search/request parameters])
def top_view(request):  # list of dicts
	return Response(zotero.top())

@api_view(["GET"])
def publications_view(request):  # list of dicts
	return Response(zotero.publications())

@api_view(["GET"])  ### ([search/request parameters])
def trash_view(request):  # list of dicts
	return Response(zotero.trash())

# error: "Response: 'since' parameter must be provider"
@api_view(["GET"])  ###  ([search/request parameters])
def deleted_view(request):  # list of dicts
	return Response(zotero.deleted())

@api_view(["GET"])  ### (itemID, [search/request parameters])
def item_view(request, item_id):  # list of dicts
	return Response(zotero.item(item_id))

@api_view(["GET"])  ### (itemID, [search/request parameters])
def children_view(request, item_id): # list of dicts
	return Response(zotero.children(item_id))

@api_view(["GET"])  ### (collectionID, [search/request parameters])
def collection_items_view(request, collection_id):  # list of dicts
	return Response(zotero.collection_items(collection_id))

@api_view(["GET"])  ### (collectionID, [search/request parameters])
def collection_items_top_view(request, collection_id):  # list of dicts
	return Response(zotero.collection_items_top(collection_id))

@api_view(["GET"])  ### (itemID, [search/request parameters])
def get_subset_view(request, item_id):  # list of dicts
	return Response(zotero.get_subset([item_id]))

# ------------------------------ Retrieving Files:
# error: "Response: Item is not an attachment"
@api_view(["GET"])  ### (itemID[, search/request parameters])
def file_view(request, item_id):  # binary string
	return Response(zotero.file(item_id))

# error: "Response: Item is not an attachment"
@api_view(["GET"])  ### (itemID[, filename, path])
def dump_view(request, item_id):  # string
	return Response(zotero.dump(item_id))

# ------------------------------ Retrieving Collections:
@api_view(["GET"])  ### ([search/request parameters]
def collections_view(request):  # list of dicts
	return Response(zotero.collections())

@api_view(["GET"])  ### ([search/request parameters]
def collections_top_view(request):  # list of dicts
	return Response(zotero.collections_top())

@api_view(["GET"])  ### (collectionID[, search/request parameters])
def collection_view(request, collection_id):  # dict
	return Response(zotero.collection(collection_id))

@api_view(["GET"])  ### (collectionID[, search/request parameters])
def collections_sub_view(request,collection_id):  # dict
	return Response(zotero.collections_sub(collection_id))

@api_view(["GET"])  ### ([collectionID])
def all_collections_view(request):  # list of dicts
	return Response(zotero.all_collections())

# ------------------------------ Retrieving Groups:
@api_view(["GET"])  ### ([search/request parameters]
def groups_view(request):  # list of dicts
	return Response(zotero.groups())

# ------------------------------ Retrieving Tags:
@api_view(["GET"])  ### ([search/request parameters]
def tags_view(request):  # list of strings
	return Response(zotero.tags())

@api_view(["GET"])  ### (itemID[, search/request parameters])
def item_tags_view(request, item_id):  # list of strings
	return Response(zotero.item_tags(item_id))

# ------------------------------ Retrieving Version Information:
@api_view(["GET"])  ### ([search/request parameters]
def item_versions_view(request):  # dict: str -> int
	return Response(zotero.item_versions())

@api_view(["GET"])  ### (itemID[, search/request parameters])
def collection_versions_view(request, item_id):  # dict: str -> int
	return Response(zotero.collection_versions(itemID=item_id))  # problem with positional argument

# ------------------------------ Full-Text Content:
@api_view(["GET"])  ### (since)
def new_fulltext_view(request, since):  # rtype - dict: str -> int
	return Response(zotero.new_fulltext(since))

# error: ResourceNotFound
@api_view(["GET"])  ### (itemID[, search/request parameters])
def fulltext_item_view(request, item_id):  # rtype - bool
	return Response(zotero.fulltext_item(item_id))

@api_view(["GET"])
def set_fulltext_view(request, item_id, payload):
	return Response(zotero.set_fulltext(item_id, payload))


## The follow() and everything() methods is currently experimental
## The iterfollow() and makeiter() for user who prefer to work with generators


# ------------------------------ Retrieving Item Counts (retrieve item counts for subset of a library):
@api_view(["GET"])
def num_items_view(request):  # int
	return Response(zotero.num_items())

@api_view(["GET"])  ### (collectionID)
def num_collectionitems_view(request, collection_id):  # int
	return Response(zotero.num_collectionitems(collection_id))

# ------------------------------ Retrieving Last Modified Version:
@api_view(["GET"])
def last_modified_version_view(request):  # int
	return Response(zotero.last_modified_version())

# ------------------------------ Search / Request Parameters for Read API calls:
# https://pyzotero.readthedocs.io/en/latest/#search-request-parameters-for-read-api-calls - for more information
@api_view(["GET"])
def add_parameters_view(request):  # list of HTML strings or None.
	return Response(zotero.add_parameters())

# -------- item_id = key ---------------------------- "UDNHQ96Z"
# -------- collection id = collections (list)  ---------- "2DA7TCXG"
