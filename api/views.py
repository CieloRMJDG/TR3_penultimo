from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics

# Asegúrate de crear este archivo: api/serializers.py
from .serializers import RegisterSerializer, ProductoSerializer 
from .models import Producto 

# --- A. VISTA DE REGISTRO (AllowAny) ---
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny] 
    serializer_class = RegisterSerializer
    
    # ... (método post opcional, pero con el serializer es suficiente)

# --- B. VISTA PROTEGIDA (Test de JWT) ---
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        content = {
            'message': '¡Ruta protegida! JWT válido.',
            'user': request.user.username,
        }
        return Response(content)

# --- C. VISTA DE PRODUCTOS (Requiere JWT) ---
class ProductoListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer