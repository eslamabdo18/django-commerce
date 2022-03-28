from django.db.transaction import atomic
from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import CustomerRegistrationSerializer, CustomerSerializer
from .models import User, Customer

# Create your views here.
from .services import CustomerService


class CustomerViews(generics.GenericAPIView):

    @swagger_auto_schema(request_body=CustomerRegistrationSerializer, responses={201: CustomerSerializer()})
    def post(self, request):
        print(request.headers)
        serializer = CustomerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, role=User.RoleChoices.CUSTOMER)
        guest_id = request.session.get('guest_user_id', None)
        customer = CustomerService.create_or_update_customer(user=user, guest_id=guest_id)
        return Response({'payload': CustomerSerializer(customer).data}, status=status.HTTP_201_CREATED)


class CustomerDataViews(generics.GenericAPIView):
    @swagger_auto_schema(responses={201: CustomerSerializer()})
    @atomic
    def get(self, request):
        if not request.user.is_anonymous:
            customer = Customer.objects.get(user=request.user)
            return Response({'payload': CustomerSerializer(customer).data}, status=status.HTTP_200_OK)
        if request.session.get('guest_user_id', None):
            guest = Customer.objects.get(_id=str(request.session['guest_user_id']))
            return Response({'payload': CustomerSerializer(guest).data}, status=status.HTTP_200_OK)
        guest = Customer.objects.create()
        request.session['guest_user_id'] = str(guest._id)
        return Response({'payload': CustomerSerializer(guest).data}, status=status.HTTP_201_CREATED)

# TODO: ADD SELLER VIEW HERE LATER
