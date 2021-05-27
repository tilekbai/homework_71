from django.shortcuts import render
from rest_framework import generics

from .serializers import *
from shop.models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class AddProductsOrdersView(generics.CreateAPIView):
    serializer_class = AddOrdersSerializer

class DetailProductsOrderView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = ListOrdersSerializer