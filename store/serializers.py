# from django.contrib.admin import display

from .models import Product, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'author', 'category', 'image', 'price', 'discounted_price', 'description')
        read_only_fields = ['author']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'products')
        # read_only_fields = ['products']
