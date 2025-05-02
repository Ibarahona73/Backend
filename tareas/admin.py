from django.contrib import admin
from .models import Tarea
# Register your models here.
#para que se vea en el admin de django (pueda usar el crud)
admin.site.register(Tarea)