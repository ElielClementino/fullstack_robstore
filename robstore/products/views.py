# coding: utf-8
import json

from django.http import JsonResponse
from ..commons.django_views_utils import ajax_login_required
from django.views.decorators.http import require_POST

from .service import product_svc


@ajax_login_required
@require_POST
def add_product(request):
    product = json.loads(request.body.decode())
    new_product = product_svc.add_product(product)
    return JsonResponse(new_product)


def list_products(request):
    products = product_svc.list_products()
    return JsonResponse({"products": products})


@ajax_login_required
@require_POST
def filter_products(request):
    products = json.loads(request.body.decode())
    filtered_data = []
    for product in products:
        filtered_data.append(product[0])
    filtered_products = product_svc.filter_products(filtered_data)

    return JsonResponse({"products":filtered_products})

@ajax_login_required
def buy_products(request):
    products_to_actualize = json.loads(request.body.decode())
    actualized_products = product_svc.buy_products(products_to_actualize)
    return JsonResponse({"actualized_products":actualized_products})
