from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SalidaListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensaje": "Aquí se listarán las salidas"})

    def post(self, request):
        return Response({"mensaje": "Aquí se registrará una salida"})

# Create your views here.
