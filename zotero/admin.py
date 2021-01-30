from django.contrib import admin

# Register your models here.
from .models import zotero_model

admin.site.register(zotero_model)

"""
from zotero.admin import TagInlineAdmin

inlines = (
	TagInlineAdmin
)
"""