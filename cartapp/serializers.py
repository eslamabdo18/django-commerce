from rest_framework import serializers

from cartapp.models import Cart, CartItem
from store.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'price', 'total_price', 'product')
        # read_only = ('price', 'total_price')


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'uuid', 'status', 'expires', 'cart_items')
