from rest_framework import serializers
from .models import Cart,Cart_Detail,Order,Order_Detail,Copoun


class CartDetailSerializers(serializers.ModelSerializer):
    class  Meta:
        model=Cart_Detail
        fields='__all__'

class CartSerializers(serializers.ModelSerializer):
    detatil_cart=CartDetailSerializers(many=True)
    class Meta:
        model=Cart
        fields='__all__'


class OrderDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model=Order_Detail
        fields='__all__'
    
class OrderSerializers(serializers.ModelSerializer):
    detatil_order=OrderDetailSerializers(many=True)
    
    copoun=serializers.StringRelatedField()
    delivery_address=serializers.StringRelatedField()
    class Meta:
        model=Order
        fields='__all__'


