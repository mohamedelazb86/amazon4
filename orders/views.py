from django.shortcuts import render,redirect
from .models import Cart,Cart_Detail,Copoun
from settings.models import Deliver_Fee
from django.shortcuts import get_object_or_404
import datetime
from products.models import Product

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

    if request.method =='POST':
        copoun_code=request.POST['copoun_code']
        #copoun=Copoun.objects.get(code=copoun_code)
        copoun=get_object_or_404(Copoun,code=copoun_code)
        if copoun and copoun.quantity > 0:
            today=datetime.datetime.today().date()
            if today >= copoun.start_date and today <= copoun.end_date :
                copoun_value=cart.cart_total /100*copoun.discount
                subtotal = cart.cart_total - copoun_value

                total = subtotal + delivery_fee

                cart.copoun=copoun
                cart.total_with_copon=subtotal
                cart.save()

                copoun.quantity -=1
                copoun.save()

              
                return render(request,'orders/checkout.html',{
                'cart':cart,
                'cart_detail':cart_detail,
                'delivery_fee':delivery_fee,
                'subtotal':subtotal,
                'discount':copoun_value,
                'total':total,
                        })




        

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


def add_to_cart(request):
    product=Product.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail,created=Cart_Detail.objects.get_or_create(cart=cart,product=product)

    cart_detail.quantity=quantity
    cart_detail.total=round(product.price * cart_detail.quantity,2)

    cart_detail.save()

    return redirect(f'/products/{product.slug}')