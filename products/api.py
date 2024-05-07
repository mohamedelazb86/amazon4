from rest_framework import generics
from .serializers import BrandListSerializer,BrandDetailSerializers,ProductdetailSerializer,ProductListSerializer
from .models import Brand,Product
from .mypagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand', 'flag']

class ProductDetaiApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductdetailSerializer


class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializer
    pagination_class=MyPagination

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name',]

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', ]

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['username', 'email']



class BrandDetailapi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializers

