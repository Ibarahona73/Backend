from django.urls import path, include
from django.contrib import admin
from .views import TareasView #importacion de la vista de las tareas
from rest_framework.routers import DefaultRouter #importacion del router



router = DefaultRouter() #creacion del router
router.register(r'tareas', TareasView, basename='tareas') 

# r'tareas' es la ruta de la api
# TareasView es la vista de las tareas
# basename='tareas' es el nombre de la ruta


#Creacion de las rutas de la api
urlpatterns = [
    path("api/v1/", include(router.urls)), #ruta de la api
    path('admin/', admin.site.urls), #ruta del admin
    
]

