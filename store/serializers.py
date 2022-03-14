# from django.contrib.admin import display

from .models import Product, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'description')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','title', 'author', 'category', 'image', 'price', 'discounted_price','description')
        read_only_fields = ('author')
