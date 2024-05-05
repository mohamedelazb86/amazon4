from django.urls import path
from .views import Product_Detail,Product_List,Brand_Detail,Brand_list
from .api import BrandDetailapi,BrandListApi,ProductDetaiApi,ProductListApi

urlpatterns = [
    path('brands/',Brand_list.as_view()),
    path('brands/<slug:slug>',Brand_Detail.as_view()),

    
    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),

    # api
    path('api/list',ProductListApi.as_view()),
    path('api/detail/<int:pk>',ProductDetaiApi.as_view()),

    path('api/brands',BrandListApi.as_view()),
    path('api/brands/<int:pk>',BrandDetailapi.as_view()),
]
