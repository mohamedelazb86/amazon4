from django.shortcuts import render
from .models import Cart,Cart_Detail
from settings.models import Deliver_Fee

from .models import Order,Order_Detail

def order_list(request):
    orders=Order.objects.filter(user=request.user)

    context={
        'orders':orders
    }
    return render(request,'orders/orderlist.html',context)


def checkout(request):
    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail=Cart_Detail.objects.filter(cart=cart)
    delivery_fee=Deliver_Fee.objects.last().fee

    subtotal=cart.cart_total
    discount=0
    total=subtotal+delivery_fee



    context={
        'cart':cart,
        'cart_detail':cart_detail,
        'delivery_fee':delivery_fee,
        'subtotal':subtotal,
        'discount':discount,
        'total':total,
    }
    return render(request,'orders/checkout.html',context)