from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="media")

    def __str__(self):
        return self.nombre