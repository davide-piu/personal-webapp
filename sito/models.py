from django.db import models

class Articolo(models.Model):
    titolo=models.CharField(max_length=200)
    autore=models.TextField()
    pub_date=models.DateField('data pubblicazione')
    corpo=models.TextField()



# Create your models here.
