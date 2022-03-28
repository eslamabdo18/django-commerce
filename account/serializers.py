from abc import ABC

from rest_framework import serializers

from account.models import Customer
from cartapp.serializers import CartSerializer


class CustomerRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=True, )
    confirm_password = serializers.CharField(write_only=True, required=True, )
    first_name = serializers.CharField(write_only=True, required=True, )
    last_name = serializers.CharField(write_only=True, required=True, )

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        data.pop('confirm_password')
        return data

    class Meta:
        ref_text = 'Customer Input Serializer'


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    cart = serializers.SerializerMethodField()

    def get_first_name(self, obj):
        return obj.user.first_name if obj.user else None

    def get_last_name(self, obj):
        return obj.user.last_name if obj.user else None

    def get_email(self, obj):
        return obj.user.email if obj.user else None

    def get_cart(self, obj):
        print(obj.cart.first())
        return CartSerializer(obj.cart.last()).data if obj.cart.last() else None

    class Meta:
        model = Customer
        fields = '__all__'
