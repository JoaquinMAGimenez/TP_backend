from django.db import models

class Superhero(models.Model):
    nombre = models.CharField (max_length=50)
    alias = models.CharField (max_length=100)
    poder = models.IntegerField()
    