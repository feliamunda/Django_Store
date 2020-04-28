from django.shortcuts import render
from django.http import JsonResponse

from apps.orders.decorators import get_cart_and_order
from .models import PromoCode

# Create your views here.

@get_cart_and_order
def validate(request, cart, order):
    code = request.GET.get('code')
    promo_code = PromoCode.objects.get_valid()

    if promo_code is None:
        return JsonResponse({
        'status' : 'False'
    }, status=404)
    
    order.apply_promo_code(promo_code)

    return JsonResponse({
        'status' : 'True',
        'code' : promo_code.code,
        'discount' : promo_code.discount,
        'total' : order.total
    }, status=500)