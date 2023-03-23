# coding: utf-8
from django.contrib import auth
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .service import accounts_svc, wallet_svc
from ..products.service import log_svc


@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


@require_POST
def register(request):
    account = accounts_svc.register(json.loads(request.body.decode()))
    return account


def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d


def get_wallet_info(request):
    data = json.loads(request.body.decode())
    wallet = wallet_svc.get_wallet_info(data)
    response = {
        "id": wallet.id,
        "user_id":wallet.user_id,
        "amount_stored": wallet.amount_stored
    }
    return JsonResponse(response)


def deposit_wallet_money(request):
    data = json.loads(request.body.decode())
    wallet_deposit = wallet_svc.deposit_wallet_money(data)
    return JsonResponse(wallet_deposit)


def withdraw_wallet_money(request):
    data = json.loads(request.body.decode())
    wallet_withdraw = wallet_svc.withdraw_wallet_money(data)
    return JsonResponse(wallet_withdraw)
