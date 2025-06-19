from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


def autenticar_usuario(request, email, password):
    user = authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        return {"data": {"message": "Login exitoso", "user": user.email}, "status": 200}
    return {"data": {"error": "Credenciales inválidas"}, "status": 401}


def registrar_usuario(data):
    required_fields = ["email", "password", "first_name", "last_name", "calle", "fecha_nac"]
    for field in required_fields:
        if not data.get(field):
            return {"data": {"error": f"El campo '{field}' es obligatorio."}, "status": 400}

    if User.objects.filter(email=data["email"]).exists():
        return {"data": {"error": "Ya existe un usuario con este correo."}, "status": 400}

    try:
        User.objects.create(
            email=data["email"],
            password=make_password(data["password"]),
            first_name=data["first_name"],
            last_name=data["last_name"],
            calle=data["calle"],
            fecha_nac=data["fecha_nac"],
        )
        return {"data": {"message": "Usuario registrado exitosamente"}, "status": 201}
    except Exception as e:
        return {"data": {"error": f"Error del servidor: {str(e)}"}, "status": 500}