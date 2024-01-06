from django.db import models
from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

    # python3 manage.py makemigrations
    # python3 manage.py migrate

class Danisanlar(models.Model):
    ad_soyad = models.CharField(max_length=100)
    boy = models.FloatField()
    kilo = models.FloatField()
    email = models.EmailField()

    def __str__(self):
        return self.ad_soyad
