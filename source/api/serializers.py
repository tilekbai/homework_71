from rest_framework import serializers
from shop.models import Product, Order, OrderProducts

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')
        read_only_fields = ['id']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price')


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category')


class AddOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ('id', 'product', 'quantity', 'order')
        read_only_fields = ['id']

class ListOrdersSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = OrderProducts
        fields = ('__all__')


class DetailOrderSerializer(serializers.ModelSerializer):
    order = ListOrdersSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'user_order', 'user_name', 'phone', 'address', 'created_at', 'order')
        read_only_fields = ['id', 'created_at']

class CreateOrderSerializer(serializers.ModelSerializer):
    order = ListOrdersSerializer()
    class Meta:
        model = Order
        fields = ('user_order', 'user_name', 'phone', 'address', 'order')
        read_only_fields = ['id', 'created_at']

