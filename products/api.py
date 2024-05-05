from rest_framework import generics
from .serializers import BrandListSerializer,BrandDetailSerializers,ProductdetailSerializer,ProductListSerializer
from .models import Brand,Product

class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer

class ProductDetaiApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductdetailSerializer


class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializer

class BrandDetailapi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializers

    