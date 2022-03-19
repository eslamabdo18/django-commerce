from abc import ABC

from rest_framework import serializers


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
