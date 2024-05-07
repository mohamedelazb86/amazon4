from django.shortcuts import render

from .models import Order,Order_Detail

def order_list(request):
    orders=Order.objects.filter(user=request.user)

    context={
        'orders':orders
    }
    return render(request,'orders/orderlist.html',context)


def checkout(request):
    return render(request,'orders/checkout.html',{})