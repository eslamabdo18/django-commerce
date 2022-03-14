from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from account.models import User, Customer, Seller


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'address')


#
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number',)
