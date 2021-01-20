from django.db import models

# Create your models here.
class Tpe_col_cattdisp(models.Model):
    id = models.AutoField(verbose_name='ID', auto_created=True, primary_key=True)
    dispositionType = models.CharField(max_length=30)
    
    def __str__(self):
        return self.id
