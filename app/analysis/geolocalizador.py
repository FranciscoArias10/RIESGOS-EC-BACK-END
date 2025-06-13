from geopy.geocoders import Nominatim

class GeoLocalizador:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="app_incidentes")

    def obtener_zona(self, latitud, longitud):
        try:
            location = self.geolocator.reverse((latitud, longitud), language='es')
            if location and "address" in location.raw:
                direccion = location.raw["address"]
                return (
                    direccion.get("neighbourhood")
                    or direccion.get("suburb")
                    or direccion.get("city")
                    or direccion.get("town")
                    or "Zona desconocida"
                )
        except Exception as e:
            print(f"Error en geolocalización: {e}")
        return "Zona desconocida"
