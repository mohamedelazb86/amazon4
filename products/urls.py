from django.urls import path
from .views import Product_Detail,Product_List,Brand_Detail,Brand_list

urlpatterns = [
    path('brands/',Brand_list.as_view()),
    path('brands/<slug:slug>',Brand_Detail.as_view()),

    
    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
]
