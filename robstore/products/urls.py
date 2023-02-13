from django.urls import path

from . import views

urlpatterns = [
    path("add/product", views.add_product),
    path("list/products", views.list_products),
    path("filter/products", views.filter_products),
    path("buy/products", views.buy_products),
]
