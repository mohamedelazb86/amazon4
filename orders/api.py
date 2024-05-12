from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import datetime
from .models import Cart,Cart_Detail,Order,Order_Detail,Copoun
from settings.models import Deliver_Fee
from products.models import Product
from accounts.models import Address
from django.shortcuts import get_object_or_404
from .serializers import CartDetailSerializers,CartSerializers,OrderDetailSerializers,OrderSerializers

class OrderListApi(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers


    def get_queryset(self):
        user=User.objects.get(username=self.kwargs['username'])
        queryset = super(OrderListApi, self).get_queryset()
        queryset = queryset.filter(user=user) 
        return queryset


class OrderDetailApi(generics.RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers



class Apply_Copoun(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        copoun_code=request.data['copoun_code']
        delivery_fee=Deliver_Fee.objects.last().fee
        #copoun=Copoun.objects.get(code=copoun_code)
        copoun=get_object_or_404(Copoun,code=copoun_code)
        cart=Cart.objects.get(user=user,status='Inprogress')
        cart_detaiL=Cart_Detail.objects.filter(cart=cart)
        if copoun and copoun.quantity > 0:
            today=datetime.datetime.today().date()
            if today >= copoun.start_date and today <= copoun.end_date:
                copoun_value=cart.cart_total /100 * copoun.discount
                sub_total=cart.cart_total - copoun_value
                total=sub_total + delivery_fee

                cart.copoun=copoun_value

                cart.total_with_copon=sub_total

                cart.save()

                copoun.quantity -=1
                copoun.save()

                return Response ({'message':'copoun ok done '},status=status.HTTP_201_CREATED)
            else:
                return Response ({'message':'sorry copoun expired'},status=status.HTTP_401_UNAUTHORIZED)
        return Response ({'message':'sorry this copoun not found pls try agin'},status=status.HTTP_404_NOT_FOUND)
    

class Create_Order(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        cart=Cart.objects.get(user=user,status='Inprogress')
        cart_detail=Cart_Detail.objects.filter(cart=cart)
        code=request.data['payement_code']
        delivery_address_id=request.data['address_id']
        delivery_address=Address.objects.get(id=delivery_address_id)


        new_order=Order.objects.create(
            user=user,
            code=code,
            delivery_address=delivery_address,
            copoun=cart.copoun,
            total=cart.cart_total,
            total_with_copoun=cart.total_with_copon,
                        
        )

        for item in cart_detail:
            product=Product.objects.get(id=item.product.id)
            Order_Detail.objects.create(
                order=new_order,
                product=product,
                quantity=item.quantity,
                price=product.price,
                total=product.price * item.quantity
            )

            product.quantity -=item.quantity
            product.save()
        cart.status='Completed'
        cart.save()

        return Response({'message':'ok daone create new_order'},status=status.HTTP_201_CREATED)


class Get_Update_Delete_Cart(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):    # get or create cart
        user=User.objects.get(username=self.kwargs['username'])
        cart,created=Cart.objects.get_or_create(user=user,status='Inprogress')
        data=CartSerializers(cart).data
        return Response({'cart':data})

    def add_update(self,request,*args,**kwargs):
        # add or update to cart detatil

        user=User.objects.get(username=self.kwargs['username'])
        product=Product.objects.get(id=request.data['product_id'])
        quantity=int(product.quantity)

        cart=Cart.objects.get(user=user,status='Inprogress')
        cart_detail,created=Cart_Detail.objects.get_or_create(cart=cart,product=product)

        cart_detail.quantity=quantity
        cart_detail.total=cart_detail.quantity * product.price

        cart_detail.save()

        return Response({'message':'ok done add and update product in cart_detail'},status=status.HTTP_202_ACCEPTED)
        

    def delete(self,request,*args,**kwargs):
        # delete from cart_detail
        user=User.objects.get(username=self.kwargs['username'])
        cart=Cart.objects.get(user=user,status='Inprogress')
        cart_detail=Cart_Detail.objects.filter(cart=cart)

        product=Cart_Detail.objects.get(id=request.data['product_id'])
        product.delete()

        product.save()

        return Response({'message':'ok delete from cart_detail'})
       
            