# Riesgos EC
Este repositorio contiene la **parte del backend** de nuestro proyecto, desarrollada con **Django**. Aquí se manejan la lógica del servidor, la gestión de la base de datos y las APIs que consumirá el frontend.
## Autores
- [Francisco Steven Arias Perez](https://github.com/FranciscoArias10)
- [Andy Bryan Chafla Guaman](https://github.com/Andy-1402)
- [Darly Douglas Farias Mendoza](https://github.com/Darly23)


##  Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto localmente:

-  **Clona el repositorio**

```bash
git clone https://github.com/FranciscoArias10/RIESGOS-EC-BACK-END.git
```

- **Entra a la carpeta del proyecto**
```bash
    cd RIESGOS-EC-BACK-END-main
```

- **Crea y activa un entorno virtual**
```bash
    python -m venv env
    # En Windows
        .\env\Scripts\activate
    # En macOS / Linux
        source env/bin/activate
```
- **Instala las dependencias**
```bash
   pip install -r requirements.txt
```
- **Aplica las migraciones de la base de datos**
```bash
   python manage.py migrate
```
- **(Opcional) Crea un superusuario para acceder al panel administrativo**
```bash
   python manage.py createsuperuser
```
- **Ejecuta el servidor de desarrollo**
```bash
   python manage.py runserver
```

## Descripción del proyecto 
Riesgos EC es una innovadora plataforma web desarrollada con React y Django REST Framework, diseñada para revolucionar la seguridad y el control del transporte en Ecuador. Este proyecto combina tecnología avanzada y usabilidad para ofrecer a los usuarios una herramienta poderosa que les permita conocer en tiempo real las zonas más peligrosas por donde se desplazan. Con funciones destacadas como el Top 10 de calles más peligrosas, la plataforma identifica y visualiza las áreas con mayor índice de riesgos, ayudando a los ciudadanos a tomar decisiones más seguras en sus rutas diarias. Además, cuenta con un Botón de Pánico que permite reportar incidentes de forma rápida y sencilla, facilitando la alerta inmediata de emergencias en diferentes sectores del país. La inteligencia artificial integrada analiza todas las evidencias y reportes recibidos, proporcionando un análisis detallado y preciso de cada situación, lo que contribuye a una gestión más eficaz de la seguridad ciudadana. Riesgos EC no solo es una herramienta informativa, sino también un aliado activo en la prevención y respuesta ante situaciones peligrosas, con el objetivo de mejorar la calidad de vida y la tranquilidad de los habitantes de Ecuador.




![Vista previa](public/742shots_so.png)
