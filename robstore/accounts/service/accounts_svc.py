from django.contrib.auth.models import User
from django.http import JsonResponse
from ..models import Wallet

def register(user_info):
    username =  user_info["userInfo"]["username"]
    email =  user_info["userInfo"]["email"]
    password =  user_info["userInfo"]["password"]

    if User.objects.filter(username=username).exists():
        return JsonResponse({"erro": "nome de usuário já está sendo usado"})

    if User.objects.filter(email=email).exists():
        return JsonResponse({"erro": "email já está sendo usado"})

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    Wallet.objects.create(
        user = user
    )

    return JsonResponse({"sucesso": f"usuário {username}, sua conta foi criada com sucesso "})
