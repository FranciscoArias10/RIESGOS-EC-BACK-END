from rest_framework import serializers
from .models import ReporteIncidente

class ReporteIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteIncidente
        fields = '__all__'
        
