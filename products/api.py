from rest_framework import generics
from .serializers import BrandListSerializer,BrandDetailSerializers,ProductdetailSerializer,ProductListSerializer
from .models import Brand,Product
from .mypagination import MyPagination

class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer

class ProductDetaiApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductdetailSerializer


class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializer
    pagination_class=MyPagination


class BrandDetailapi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializers

