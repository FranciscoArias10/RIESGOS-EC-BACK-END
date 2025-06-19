from rest_framework import status
from app.serializers.serializers import UsuarioSerializer


def actualizar_perfil(usuario, data):
    serializer = UsuarioSerializer(usuario, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return {"data": serializer.data, "status": status.HTTP_200_OK}
    return {"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}
