from django.urls import path
from .views import APILoginView, APIRegisterView, ReporteIncidenteView,AnalisisReporteAPIView
from .views import (
    RequestPasswordResetView,
    VerifyResetCodeView,
    SetNewPasswordView,
)

# o cualquier otra vista que estés usando

urlpatterns = [
    path("login/", APILoginView.as_view(), name="api-login"),
    path("register/", APIRegisterView.as_view(), name="api-register"),
    path("solicitar-reset/", RequestPasswordResetView.as_view()),
    path("verificar-codigo/", VerifyResetCodeView.as_view()),
    path("nueva-contrasena/", SetNewPasswordView.as_view()),
    path('reporte/', ReporteIncidenteView.as_view(), name='reporte_incidente'),
    path('analisis/', AnalisisReporteAPIView.as_view(), name='analisis-reportes'),
]
