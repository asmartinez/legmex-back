from django.db import models

# Create your models here.

# Model para los documentos subidos en elastic search
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    texto = models.TextField()