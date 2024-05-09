from django.urls import path
from .views import order_list,checkout,add_to_cart
from .api import OrderDetailApi,OrderListApi


urlpatterns = [
    path('',order_list),
    path('checkout',checkout),
    path('add_to_cart',add_to_cart),

    # api
    path('api/<str:username>/list',OrderListApi.as_view()),
    path('api/<str:username>/<int:pk>',OrderDetailApi.as_view()),

 
  
]
