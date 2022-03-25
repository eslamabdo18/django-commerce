from decimal import Decimal

import null
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# from store.models import Product


class Cart(models.Model):
    class StatusTypes(models.IntegerChoices):
        CURRENT = 0, 'Current'
        COMPLETE = 1, 'Complete'

    status = models.IntegerField(choices=StatusTypes.choices, )
    expires = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('1.00'))])
    total_price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('1.00'))])
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name=_('cart_item'))
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name=_('cart_items'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    class StatusTypes(models.IntegerChoices):
        PENDING = 0, 'Current'
        COMPLETE = 1, 'Complete'

    status = models.IntegerField(choices=StatusTypes.choices, )
    cost = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('1.00'))])
    delivery_fees = models.DecimalField(decimal_places=2, max_digits=8, null=True,
                                        validators=[MinValueValidator(Decimal('1.00'))])
    tax = models.DecimalField(decimal_places=2, max_digits=8, null=True,
                              validators=[MinValueValidator(Decimal('0'))])

    total = models.DecimalField(decimal_places=2, max_digits=8, null=True,
                                validators=[MinValueValidator(Decimal('0'))])

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name=_('orders'))

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name=_('orders'))

    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name=_('orders'))
    # payment =

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
