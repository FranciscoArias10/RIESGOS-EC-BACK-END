from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .managers import UsuarioManager  # 👈 Importa el manager personalizado


class Usuarios(AbstractUser):
    username = None  # Elimina el campo username
    email = models.EmailField(unique=True)
    fecha_nac = models.DateField(blank=True)
    calle = models.CharField(max_length=80)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name"
    ]  # Puedes agregar "last_name" si lo haces obligatorio

    objects = UsuarioManager()  # Usa el manager personalizado

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Recuperar_contrasena(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=5)
    created_at = models.DateTimeField(default=timezone.now)

    def validar(self):
        return timezone.now() - self.created_at < timezone.timedelta(minutes=10)

    def __str__(self):
        return f"Código {self.codigo} para {self.usuario.email}"
