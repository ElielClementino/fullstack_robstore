from django.contrib.auth.models import User
from django.http import JsonResponse

def register(user_info):
    username =  user_info["userInfo"]["username"]
    email =  user_info["userInfo"]["email"]
    password =  user_info["userInfo"]["password"]

    if User.objects.filter(username=username).exists():
        return JsonResponse({"erro": "nome de usuário já está sendo usado"})

    if User.objects.filter(email=email).exists():
        return JsonResponse({"erro": "email já está sendo usado"})

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return JsonResponse({"sucesso": f"usuário {username}, sua conta foi criada com sucesso "})