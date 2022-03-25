# from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# from cartapp.models import Cart, CartItem


class CustomCartItemManager(models.Manager):
    """
    Custom cartapp model manager where we create new item if dosent exist or update
    it if it exsit
    """
    def create_or_update_item(self, cart, product, quantity=1, **extra_fields):
        cart = self.objects.get(cart=cart, product=product)
        if cart:
            qyt = quantity + cart.quantity
            self.objects.update(quantity=qyt, **extra_fields)
        else:
            self.objects.create(cart=cart, product=product,price=product.price,quantity=quantity, **extra_fields)
