from decimal import Decimal

from django.db.transaction import atomic

from store.models import Product
from .models import Cart, CartItem


class CartService:

    @staticmethod
    @atomic
    def add_to_cart(quantity: int, product: Product, cart_id: str = None):
        print(cart_id)
        cart, created = Cart.objects.get_or_create(uuid=cart_id)
        print(cart)
        # product = Product.objects.get(id=product)
        cart_item = CartItem.objects.create_or_update_item(quantity=quantity, product=product, cart=cart)

        return cart, cart_item
