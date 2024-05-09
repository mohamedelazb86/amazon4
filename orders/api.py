from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
import datetime
from .models import Cart,Cart_Detail,Order,Order_Detail,Copoun
from settings.models import Deliver_Fee
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
                