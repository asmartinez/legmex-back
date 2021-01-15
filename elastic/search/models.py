from django.db import models

# Model para los documentos subidos en elastic search
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    texto = models.TextField()
    archivo = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name

