from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse


@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({"message": "CSRF cookie set"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),  # Aquí tienes tus endpoints
    path("api/csrf/", csrf),  # CSRF Token handler
]
