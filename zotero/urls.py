# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views

# enrutamiento automático
#router = routers.DefaultRouter()
#router.register(r'zotero', views.zotero_viewset)

urlpatterns = [
#	path('router/', include(router.urls)),
#	path('api-auth/', include('rest_framework.urls', 'namespaces=rest_framework'))
	# Read API
	# items
	path('read/key_info/', views.key_info_view),
	path('read/items/', views.items_view),
	path('read/count_items/', views.count_items_view),
	path('read/top/', views.top_view),
	path('read/publications/', views.publications_view),
	path('read/trash/', views.trash_view),
	path('read/deleted/', views.deleted_view),
	path('read/item/<str:item_id>', views.item_view),
	path('read/children/<str:item_id>/', views.children_view),
	path('read/collection_items/<str:collection_id>/', views.collection_items_view),
	path('read/collection_items_top/<str:collection_id>/', views.collection_items_top_view),
	path('read/get_subset/<str:item_id>/', views.get_subset_view),
	# files
	path('read/file/<str:item_id>/', views.file_view),
	path('read/dump/<str:item_id>/', views.dump_view),
	# collections
	path('read/collections/', views.collections_view),
	path('read/collections_top/', views.collections_top_view),
	path('read/collection/<str:collection_id>/', views.collection_view),
	path('read/collections_sub/<str:collection_id>/', views.collections_sub_view),
	path('read/all_collections/', views.all_collections_view),
	# groups
	path('read/groups/', views.groups_view),
	# tags
	path('read/tags/', views.tags_view),
	path('read/item_tags/<str:item_id>/', views.item_tags_view),
	# version information
	path('read/item_versions/', views.item_versions_view),
	path('read/collection_versions/<str:item_id>/', views.collection_versions_view),
	#-full-text content
	path('read/new_fulltext/<str:since>/', views.new_fulltext_view),
	path('read/fulltext_item/<str:item_id>/', views.fulltext_item_view),
	#path('read/set_fulltest/<str:item_id>/', views.set_fulltext_view,
		# for pdf: content:<str>, indexedPages:<int>, totalPages:<int>   ---- for documents:
	#	payload={'content': 'content in this place', 'indexedChars': '<int>', 'totalChars': '<int>'}),
	# item counts
	path('read/num_items/', views.num_items_view),
	path('read/num_collectionitems/<str:collection_id>/', views.num_collectionitems_view),
	path('read/last_modified_version/', views.last_modified_version_view),
	path('read/add_parameters/', views.add_parameters_view),
]