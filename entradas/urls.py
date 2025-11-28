# entradas/urls.py
from django.urls import path
from .views import EntradaListCreateView

urlpatterns = [
    path('', EntradaListCreateView.as_view(), name='entrada_list_create'),
]
