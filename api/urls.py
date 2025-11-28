# api/urls.py

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)

# IMPORTANTE: Asegúrate de que estas vistas existan en api/views.py
# (O el error de importación será el siguiente)
from .views import RegisterView, ProtectedView, ProductoListCreateView 

# Define la lista de patrones de URL
urlpatterns = [
    # --- CORE AUTH (ABIERTO) ---
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # LOGIN
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # --- CORE PROTEGIDO ---
    path('protected/', ProtectedView.as_view(), name='protected_route'),
    path('productos/', ProductoListCreateView.as_view(), name='product_list_create'), 

    # --- INCLUSIÓN DE APPS FUNCIONALES ---
    # Estos archivos (entradas/urls.py y salidas/urls.py) también deben existir
    path('entradas/', include('entradas.urls')),
    path('salidas/', include('salidas.urls')),
]