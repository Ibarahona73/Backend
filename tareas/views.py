from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarea
from .serializer import TareaSerializer

class TareasView(viewsets.ModelViewSet):
    queryset = Tarea.objects.all() #todos los datos de la tabla tarea
    serializer_class = TareaSerializer #serializador de la tabla tarea

