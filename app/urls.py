from django.urls import path
from .views import (
    APILoginView,
    APIRegisterView,
    RequestPasswordResetView,
    VerifyResetCodeView,
    SetNewPasswordView,
    PerfilView,
)
from django.conf import settings
from django.conf.urls.static import static
from .views import ReporteIncidenteView
from .views import AnalisisReporteAPIView


urlpatterns = [
    path("login/", APILoginView.as_view(), name="api-login"),
    path("registro/", APIRegisterView.as_view(), name="registro"),
    path("solicitar-reset/", RequestPasswordResetView.as_view()),
    path("verificar-codigo/", VerifyResetCodeView.as_view()),
    path("nueva-contrasena/", SetNewPasswordView.as_view()),
    path("perfil/", PerfilView.as_view(), name="perfil"),
    path('reporte/', ReporteIncidenteView.as_view()),
    path('analisis/', AnalisisReporteAPIView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
