from rest_framework import serializers

from cartapp.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'quantity', 'price', 'total_price', 'product_id')
        # read_only = ('price', 'total_price')


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'status', 'expires', 'cart_items')

