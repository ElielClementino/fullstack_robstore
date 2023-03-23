from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login),
    path("register", views.register),
    path("logout", views.logout),
    path("whoami", views.whoami),
    path("wallet-info", views.get_wallet_info),
    path("wallet-deposit", views.deposit_wallet_money),
    path("withdraw-wallet-money", views.withdraw_wallet_money)
]
