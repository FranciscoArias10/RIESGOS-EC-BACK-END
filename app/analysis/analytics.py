import pandas as pd
from .geolocalizador import GeoLocalizador

class AnalizadorReportes:
    def __init__(self, queryset):
        self.df = pd.DataFrame(list(queryset.values()))
        self.geo = GeoLocalizador()
        self._preprocesar()

    def _preprocesar(self):
        self.df['fecha_reporte'] = pd.to_datetime(self.df['fecha_reporte'])
        self.df['hora'] = self.df['fecha_reporte'].dt.hour
        self.df['dia'] = self.df['fecha_reporte'].dt.day_name()

        if 'zona' not in self.df.columns:
            self.df['zona'] = self.df.apply(lambda row: self.geo.obtener_zona(row['latitud'], row['longitud']), axis=1)
        else:
            self.df['zona'] = self.df.apply(
                lambda row: row['zona'] if row['zona'] else self.geo.obtener_zona(row['latitud'], row['longitud']),
                axis=1
            )

    def tipo_mas_comun(self):
        return self.df['tipo_incidente'].value_counts().idxmax()

    def hora_pico(self):
        return self.df['hora'].value_counts().idxmax()

    def zona_mas_incidentes(self):
        return self.df['zona'].value_counts().idxmax()

    def resumen(self):
        return {
            "tipo_incidente_mas_comun": self.tipo_mas_comun(),
            "hora_pico": self.hora_pico(),
            "zona_mas_reportada": self.zona_mas_incidentes()
        }
