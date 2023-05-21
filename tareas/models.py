from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=20)
    nombre=models.CharField(max_length=50)
    razon_social=models.TextField(blank=True)
    clave_sii=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    telefono=models.CharField(max_length=20)
    estado=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
