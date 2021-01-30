from django.db import models

# Model para los documentos subidos en elastic search
class Biblioteca(models.Model):
    dispositionTitle = models.CharField(max_length=155, blank=True)
    date = models.CharField(max_length=155, blank=True)
    volume = models.CharField(max_length=155, blank=True)
    pageNumbers = models.CharField(max_length=155, blank=True)
    legislationTranscriptOriginal = models.FileField(blank=True, null=False)
    legislationTranscriptCopy = models.TextField(blank=True)
    place = models.CharField(max_length=155, blank=True)
    dispositionNumber = models.CharField(max_length=155, blank=True)
    dispositionTypeId = models.CharField(max_length=155, blank=True)
    affairId = models.CharField(max_length=155, blank=True)

