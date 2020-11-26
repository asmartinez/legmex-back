from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Tpe_col_enc(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    fecha = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    usuario = models.CharField(max_length=50)