from django.conf import settings
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
# from rest_framework.authtoken.admin import User

from account.models import Seller


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField()
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(Decimal('1.00'))])
    discounted_price = models.DecimalField(decimal_places=2, max_digits=8,
                                           validators=[MinValueValidator(Decimal('1.00'))], )
    description = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title
