# entradas/urls.py

from django.urls import path
# Asumimos que esta vista será creada por Persona 2
from .views import EntradaListCreateView 

urlpatterns = [
    # Ruta principal para listar y crear entradas (PROTEGIDA)
    path('', EntradaListCreateView.as_view(), name='entrada_list_create'),
]