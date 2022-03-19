from rest_framework import generics
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import CustomerRegistrationSerializer
from .models import User


# Create your views here.


class CustomerViews(generics.GenericAPIView):

    @swagger_auto_schema(request_body=CustomerRegistrationSerializer, responses={201: 'created'})
    def post(self, request):
        serializer = CustomerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data, role=2)
        return Response(status=status.HTTP_201_CREATED)

# TODO: ADD SELLER VIEW HERE LATER
