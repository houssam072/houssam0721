from rest_framework import serializers
from .models import Product, PictureProduct

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
                  

class ProductImage(serializers.ModelSerializer):
    class Meta:
        model = PictureProduct
        fields = '__all__'
