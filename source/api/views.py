from django.shortcuts import render
from rest_framework import generics

from .serializers import ProductDetailSerializer, ProductListSerializer
from shop.models import Product

# Create your views here.

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()