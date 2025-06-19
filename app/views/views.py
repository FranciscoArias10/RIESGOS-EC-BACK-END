from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from app.services.auth_services import autenticar_usuario, registrar_usuario
from app.services.password_services import generar_codigo_recuperacion, validar_codigo, actualizar_contrasena
from app.services.profile_services import actualizar_perfil
from app.services.report_services import crear_reporte, analizar_reportes

from app.serializers.serializers import UsuarioSerializer



@method_decorator(csrf_exempt, name="dispatch")
class APILoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email y contraseña son obligatorios"}, status=400)

        resultado = autenticar_usuario(request, email, password)
        return Response(resultado["data"], status=resultado["status"])


class APIRegisterView(APIView):
    def post(self, request):
        resultado = registrar_usuario(request.data)
        return Response(resultado["data"], status=resultado["status"])


class RequestPasswordResetView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Se requiere el correo electrónico."}, status=400)

        resultado = generar_codigo_recuperacion(email)
        return Response(resultado["data"], status=resultado["status"])


class VerifyResetCodeView(APIView):
    def post(self, request):
        resultado = validar_codigo(request.data)
        return Response(resultado["data"], status=resultado["status"])


class SetNewPasswordView(APIView):
    def post(self, request):
        resultado = actualizar_contrasena(request.data)
        return Response(resultado["data"], status=resultado["status"])


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        resultado = actualizar_perfil(request.user, request.data)
        return Response(resultado["data"], status=resultado["status"])


class ReporteIncidenteView(APIView):
    def post(self, request):
        resultado = crear_reporte(request.data)
        return Response(resultado["data"], status=resultado["status"])


class AnalisisReporteAPIView(APIView):
    def get(self, request):
        resultado = analizar_reportes()
        return Response(resultado["data"], status=resultado["status"])
