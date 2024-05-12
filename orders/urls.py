from django.urls import path
from .views import order_list,checkout,add_to_cart
from .api import OrderDetailApi,OrderListApi,Apply_Copoun,Create_Order,Get_Update_Delete_Cart


urlpatterns = [
    path('',order_list),
    path('checkout',checkout),
    path('add_to_cart',add_to_cart),

    # api
    path('api/<str:username>/list',OrderListApi.as_view()),
    path('api/<str:username>/<int:pk>',OrderDetailApi.as_view()),
    path('api/<str:username>/apply_copoun',Apply_Copoun.as_view()),

    path('api/create_order/<str:username>',Create_Order.as_view()),
    path('api/update_delete_cart/<str:username>',Get_Update_Delete_Cart.as_view()),



 
  
]
