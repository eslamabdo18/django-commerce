from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from .managers import CustomUserManager

from django.db import models


# Create your models here.

class User(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 0, 'Admin'
        SELLER = 1, 'Seller'
        CUSTOMER = 2, 'Customer'

    username = models.CharField(null=True, max_length=255, blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    role = models.IntegerField(choices=RoleChoices.choices, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['password']


class Address(models.Model):
    city = models.CharField(max_length=200)
    country = CountryField()
    post_code = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='customer')
    phone_number = models.CharField(max_length=50, unique=True,null=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def post_save_receiver(sender, instance, created, **kwargs):
        # print(instance.RoleChoices.choices)
        # print(instance)
        # return
        if created and instance.role == 2:
            # print(instance)
            customer = Customer.objects.create(user=instance)

    # address = models.CharField(max_length=150, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Customers'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='seller')
    phone_number = models.CharField(max_length=50)
    national_id = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Sellers'
