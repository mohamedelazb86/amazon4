from rest_framework import generics
from django.contrib.auth.models import User
from .models import Cart,Cart_Detail,Order,Order_Detail,Copoun
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


