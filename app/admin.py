from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios, Recuperar_contrasena


class CustomUserAdmin(UserAdmin):
    model = Usuarios
    list_display = ("email", "first_name", "last_name", "is_staff", "fecha_nac")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Información personal",
            {"fields": ("first_name", "last_name", "fecha_nac", "calle")},
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "fecha_nac",
                    "calle",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Usuarios, CustomUserAdmin)
admin.site.register(Recuperar_contrasena)
