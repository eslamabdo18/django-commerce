import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
# from store.models import Product
from account.models import Customer, Address
from cartapp.managers import CustomCartItemManager
from store.models import Product


class Cart(models.Model):
    class StatusTypes(models.IntegerChoices):
        CURRENT = 0, 'Current'
        COMPLETE = 1, 'Complete'

    status = models.IntegerField(choices=StatusTypes.choices, )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    expires = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name=_('cart'), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = self.StatusTypes.CURRENT
        super(Cart, self).save(*args, **kwargs)


class CartItem(models.Model):
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('1.00'))])
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name=_('cart_item'))
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name=_('cart_items'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomCartItemManager()

    @property
    def total_price(self):
        price = Decimal(self.price * self.quantity)
        return "{:.2f}".format(price)


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

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name=_('orders'))

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name=_('orders'))
    # payment =

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
