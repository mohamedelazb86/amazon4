from rest_framework import serializers
from .models import Product,Brand,ImagePOroduct

class ImageSerializer(serializers.ModelSerializer):
    product=serializers.StringRelatedField()
    class Meta:
        model=ImagePOroduct
        fields='__all__'

class ProductListSerializer(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

class ProductdetailSerializer(serializers.ModelSerializer):
    image=ImageSerializer(source='iamge_product',many=True)
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