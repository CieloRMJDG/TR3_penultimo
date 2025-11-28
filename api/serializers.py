# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Producto, Inventario # Importa tus modelos

# --- 1. Serializador de Registro ---
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# --- 2. Serializador de Producto ---
class ProductoSerializer(serializers.ModelSerializer):
    stock_actual = serializers.IntegerField(source='inventario.stock_actual', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'stock_actual']