from django.db import models

# Create your models here.
class Registro(models.Model):
    title = models.CharField(max_length=50)
    titleDate = models.DateTimeField()
    volumen = models.TextField()
    paginas = models.TextField()
    Trasncripcion = models.TextField()
    Lugar = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    created_user = models.TextField()

    def __str__(self):
        return self.title

