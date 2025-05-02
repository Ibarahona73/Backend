from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        extra_kwargs = {
            'titulo': {
                'error_messages': {
                    'required': 'El título es requerido',
                    'blank': 'El título no puede estar vacío'
                }
            }
        }


