from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 0, 'Admin'
        SELLER = 1, 'Seller'
        CUSTOMER = 2, 'Customer'

    # username = models.CharField(null=True, max_length=255,blank=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    role = models.IntegerField(choices=RoleChoices.choices, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    #
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'password']

    # def save(self, *args, **kwargs):
    #     if self.role == self.RoleChoices.ADMIN:
    #         self.is_superuser = True
    #     super(User, self).save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='customer')
    phone_number = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=150,null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Customers'


#
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='seller')
    phone_number = models.CharField(max_length=50)
    national_id = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Sellers'
