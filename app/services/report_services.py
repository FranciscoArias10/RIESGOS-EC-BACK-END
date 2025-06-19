from rest_framework import status
from app.serializers.serializers import ReporteIncidenteSerializer
from app.models import ReporteIncidente
from app.analysis.analytics import AnalizadorReportes


def crear_reporte(data):
    serializer = ReporteIncidenteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return {"data": {"mensaje": "Reporte recibido correctamente"}, "status": status.HTTP_201_CREATED}
    return {"data": serializer.errors, "status": status.HTTP_400_BAD_REQUEST}


def analizar_reportes():
    reportes = ReporteIncidente.objects.all()
    if not reportes.exists():
        return {"data": {"error": "No hay reportes disponibles."}, "status": status.HTTP_404_NOT_FOUND}

    analizador = AnalizadorReportes(reportes)
    resumen = analizador.resumen()
    return {"data": resumen, "status": status.HTTP_200_OK}
