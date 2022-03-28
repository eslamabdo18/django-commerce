from django.contrib import admin

# Register your models here.
from cartapp.models import Cart, CartItem


@admin.register(Cart)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(CartItem)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id',)
