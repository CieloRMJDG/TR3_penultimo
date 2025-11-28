from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Entrada
from .serializers import EntradaSerializer

class EntradaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Entrada.objects.all().order_by('-fecha_entrada')
    serializer_class = EntradaSerializer

    def perform_create(self, serializer):
        serializer.save(registrado_por=self.request.user)

# Create your views here.
