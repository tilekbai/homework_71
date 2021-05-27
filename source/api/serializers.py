from rest_framework import serializers
from shop.models import Product

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ("__all__")


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category')
        read_only_fields = ('id',)