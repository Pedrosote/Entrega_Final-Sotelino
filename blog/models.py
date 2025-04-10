from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    imagen = models.ImageField(upload_to='imagenes_post/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Post(models.Model):
    class estado(models.TextChoices):
        BORRADOR = "B", "borrador"
        PUBLICADO = "P", "publicado"
    titulo = models.CharField( max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey( User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=estado.choices, default = estado.BORRADOR)
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    def __str__(self):
        return self.titulo