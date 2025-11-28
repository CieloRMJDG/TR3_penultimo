# entradas/serializers.py
from rest_framework import serializers
from .models import Entrada
from api.models import Inventario

class EntradaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = Entrada
        fields = [
            'id',
            'producto',
            'producto_nombre',
            'cantidad',
            'fecha_entrada',
            'registrado_por'
        ]
        read_only_fields = ['registrado_por', 'fecha_entrada', 'producto_nombre']

    def create(self, validated_data):
        producto = validated_data['producto']
        cantidad = validated_data['cantidad']

        # Actualizar inventario
        inventario, created = Inventario.objects.get_or_create(producto=producto)
        inventario.stock_actual += cantidad
        inventario.save()

        return super().create(validated_data)
