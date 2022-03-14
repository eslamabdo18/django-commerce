from django.shortcuts import render
from rest_framework import generics

from account.permissions import IsCustomer, IsSellerOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsSellerOrReadOnly]
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCustomer]
    print('request.user')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
