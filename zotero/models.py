from django.db import models

# Create your models here.
class zotero_model(models.Model):
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	pages = models.IntegerField()

	def __str__(self):
		return self.title