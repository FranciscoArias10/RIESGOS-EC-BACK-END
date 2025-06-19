from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app.models import Usuarios
from app.models import ReporteIncidente

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            "first_name",
            "last_name",
            "calle",
            "fecha_nac",
            "foto",
            "email",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
            "email": {"required": False},
        }

    def update(self, instance, validated_data):
        # Si se proporciona una nueva contraseña, la encriptamos
        password = validated_data.pop("password", None)
        if password:
            instance.password = make_password(password)

        return super().update(instance, validated_data)



class ReporteIncidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteIncidente
        fields = '__all__'