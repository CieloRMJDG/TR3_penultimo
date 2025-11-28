
from django.db import models
from django.contrib.auth.models import User # Para referenciar al usuario que registra

class Producto(models.Model):
    """Modelo para definir un producto en el inventario."""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    """Modelo para almacenar el stock actual de cada producto."""
    # Relación uno a uno con Producto
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, primary_key=True)
    stock_actual = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.producto.nombre}: {self.stock_actual}"