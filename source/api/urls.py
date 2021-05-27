from django.urls import path, include
from rest_framework import routers
from .views import ProductCreateView, ProductListView, ProductDetailView

app_name='api_v1'

urlpatterns = [
    path('api/v1/products/', ProductListView.as_view(), name='index'),
    path('api/v1/product/create/', ProductCreateView.as_view(), name='create-product'),
    path('api/v1/product/detail/<int:pk>/', ProductDetailView.as_view(), name ='detail-product')
]