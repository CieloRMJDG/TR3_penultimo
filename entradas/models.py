from django.db import models

from api.models import Producto
from django.contrib.auth.models import User

class Entrada(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.cantidad} unidades de {self.producto.nombre}"


# Create your models here.
