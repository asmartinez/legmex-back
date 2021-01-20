from django.db import models

# Model para los documentos subidos en elastic search
class Biblioteca(models.Model):
    dispositionTitle = models.CharField(max_length=155)
    date = models.CharField(max_length=155)
    volume = models.CharField(max_length=155)
    pageNumbers = models.CharField(max_length=155)
    legislationTranscriptOriginal = models.FileField(blank=False, null=False)
    legislationTranscriptCopy = models.TextField()
    place = models.CharField(max_length=255)
    dispositionTypeId = models.CharField(max_length=255)
    affairId = models.CharField(max_length=255)

