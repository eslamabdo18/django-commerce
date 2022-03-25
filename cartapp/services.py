from decimal import Decimal

from django.db.transaction import atomic

from store.models import Product
from .models import Cart, CartItem


class CartService:

    @staticmethod
    @atomic
    def add_to_cart(quantity: int, product_id: int, cart_id: int = None):
        cart = Cart.objects.get_or_create(id=cart_id)
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.create_or_update_item(quantity=quantity, product=product, cart=cart)

        return cart, cart_item
