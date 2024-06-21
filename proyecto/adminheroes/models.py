from django.db import models

class Superheroe(models.Model):
    nombre = models.CharField (max_length=50)
    alias = models.CharField (max_length=100)
    poder = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Universo(models.Model):
    name = models.CharField(max_length=128)
    heroes = models.ManyToManyField(Superheroe, blank=True)

    def __str__(self):
        return self.name
        
class User(models.Model):
    name = models.CharField(max_length=128)
    heroes = models.ManyToManyField(Superheroe, blank=True)

    def __str__(self):
        return self.name

