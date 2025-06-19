from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.hashers import make_password
from app.models import Usuarios, Recuperar_contrasena
import random


def generar_codigo_recuperacion(email):
    user = Usuarios.objects.filter(email=email).first()
    if not user:
        return {"data": {"error": "Usuario no encontrado con este correo."}, "status": 404}

    code = str(random.randint(10000, 99999))
    Recuperar_contrasena.objects.create(usuario=user, codigo=code)

    html_message = render_to_string("verification_email.html", {
        "verification_code": code,
        "app_name": "Riesgos EC",
    })

    send_mail(
        subject="Tu código de recuperación - Riesgos EC",
        message=f"Código de recuperación: {code}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=html_message,
    )

    return {"data": {"message": "Código enviado correctamente."}, "status": 200}


def validar_codigo(data):
    email = data.get("email")
    code = data.get("code")

    if not email or not code:
        return {"data": {"error": "Faltan campos obligatorios."}, "status": 400}

    user = Usuarios.objects.filter(email=email).first()
    if not user:
        return {"data": {"error": "Usuario no encontrado."}, "status": 404}

    registro = Recuperar_contrasena.objects.filter(usuario=user, codigo=code).last()
    if registro and registro.validar():
        return {"data": {"message": "Código válido."}, "status": 200}
    return {"data": {"error": "Código inválido o expirado."}, "status": 400}


def actualizar_contrasena(data):
    email = data.get("email")
    new_password = data.get("password")

    if not email or not new_password:
        return {"data": {"error": "Email y nueva contraseña son obligatorios."}, "status": 400}

    user = Usuarios.objects.filter(email=email).first()
    if not user:
        return {"data": {"error": "Usuario no encontrado."}, "status": 404}

    user.password = make_password(new_password)
    user.save()

    return {"data": {"message": "Contraseña actualizada correctamente."}, "status": 200}
