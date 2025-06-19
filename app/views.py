from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name="dispatch")
class APILoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"error": "Email y contraseña son obligatorios"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # IMPORTANTE: usar username=email ya que USERNAME_FIELD = 'email'
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response(
                {"message": "Login exitoso", "user": user.email},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED
            )


class APIRegisterView(APIView):
    def post(self, request):
        data = request.data
        required_fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "calle",
            "fecha_nac",
        ]

        for field in required_fields:
            if field not in data or not data[field]:
                return Response(
                    {"error": f"El campo '{field}' es obligatorio."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if User.objects.filter(email=data["email"]).exists():
            return Response(
                {"error": "Ya existe un usuario con este correo."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.create(
                email=data["email"],
                password=make_password(data["password"]),
                first_name=data["first_name"],
                last_name=data["last_name"],
                calle=data["calle"],
                fecha_nac=data["fecha_nac"],
            )
        except Exception as e:
            return Response(
                {"error": f"Error del servidor: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(
            {"message": "Usuario registrado exitosamente"},
            status=status.HTTP_201_CREATED,
        )


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import Recuperar_contrasena, Usuarios
import random
from django.template.loader import render_to_string


class RequestPasswordResetView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Se requiere el correo electrónico."}, status=400)

        user = Usuarios.objects.filter(email=email).first()
        if not user:
            return Response(
                {"error": "Usuario no encontrado con este correo."}, status=404
            )

        code = str(random.randint(10000, 99999))
        Recuperar_contrasena.objects.create(usuario=user, codigo=code)

        # Renderiza el mensaje HTML del correo
        html_message = render_to_string(
            "verification_email.html",
            {
                "verification_code": code,
                "app_name": "Riesgos EC",
            },
        )

        send_mail(
            subject="Tu código de recuperación - Riesgos EC",
            message="Código de recuperación: " + code,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            html_message=html_message,
        )

        return Response({"message": "Código enviado correctamente."})


class VerifyResetCodeView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")

        if not email or not code:
            return Response({"error": "Faltan campos obligatorios."}, status=400)

        user = Usuarios.objects.filter(email=email).first()
        if not user:
            return Response({"error": "Usuario no encontrado."}, status=404)

        registro = Recuperar_contrasena.objects.filter(usuario=user, codigo=code).last()

        if registro and registro.validar():
            return Response({"message": "Código válido."})
        else:
            return Response({"error": "Código inválido o expirado."}, status=400)


from django.contrib.auth.hashers import make_password


class SetNewPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        new_password = request.data.get("password")

        if not email or not new_password:
            return Response(
                {"error": "Email y nueva contraseña son obligatorios."}, status=400
            )

        user = Usuarios.objects.filter(email=email).first()
        if not user:
            return Response({"error": "Usuario no encontrado."}, status=404)

        user.password = make_password(new_password)
        user.save()

        return Response({"message": "Contraseña actualizada correctamente."})


# -----------------------------CODIGO PARA PAGINA DE PERFIL-------------------------------
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer  # Asegúrate de importar el serializer


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]  # acepta imagen y texto

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReporteEmergenciaSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ReporteEmergenciaAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ReporteEmergenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)