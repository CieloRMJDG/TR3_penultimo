from django.urls import path
# Asumimos que esta vista será creada por Persona 3
from .views import SalidaListCreateView 

urlpatterns = [
    # Ruta principal para listar y registrar salidas (PROTEGIDA)
    path('', SalidaListCreateView.as_view(), name='salida_list_create'),
]