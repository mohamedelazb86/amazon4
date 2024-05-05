from rest_framework import serializers
from .models import Product,Brand

class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

class ProductdetailSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

class BrandListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Brand
        fields='__all__'

class BrandDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'