from rest_framework import serializers
from .models import Chamado

class ChamadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamado
        fields = ['id', 'titulo', 'descricao', 'status', 'data_criacao']