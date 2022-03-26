# from django.shortcuts import render
# from django.views import View
from rest_framework import generics, viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
from account.models import Customer
from cartapp.models import Cart, CartItem
from cartapp.serializers import CartSerializer, CartItemSerializer
from cartapp.services import CartService


class CartIdRequestView(generics.GenericAPIView):
    @swagger_auto_schema(responses={201: 'Created'})
    def get(self, request):
        if not request.session.get('cart_id'):
            print(request.session.get('cart_id'))
            customer = Customer.objects.get(_id=request.session['guest_user_id'])
            cart = Cart.objects.create(customer=customer)
            request.session['cart_id'] = str(cart.uuid)
        return Response({'cart_id': request.session['cart_id']}, status=status.HTTP_201_CREATED)


class CartView(viewsets.ReadOnlyModelViewSet):
    http_method_names = ['get']
    lookup_field = 'uuid'
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartViewV2(generics.GenericAPIView):
    @swagger_auto_schema(responses={200: 'created'})
    def get(self, request, id):
        cart = Cart.objects.filter(uuid=id).first()
        return Response({'payload': CartSerializer(cart).data}, status=status.HTTP_200_OK)


class CartItemsViewV2(generics.GenericAPIView):
    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = CartItem
            fields = ('id', 'quantity', 'product')
            ref_name = 'cart view input'

    @swagger_auto_schema(request_body=InputSerializer, responses={201: 'created'})
    def post(self, request, id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart, cart_item = CartService.add_to_cart(**serializer.validated_data, cart_id=id)
        return Response({'payload': CartItemSerializer(cart_item, many=True).data}, status=status.HTTP_200_OK)

    # def batch(self, *args, **kwargs):


class CartItemsView(viewsets.ModelViewSet):
    class CreateInputSerializer(serializers.ModelSerializer):
        class Meta:
            model = CartItem
            fields = ('id', 'quantity', 'product')
            ref_name = 'CreateInputSerializer'

    # http_method_names = ['get']

    queryset = CartItem.objects.all().select_related('cart')

    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.action in ["create", ]:
            return self.CreateInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        cart_id = self.kwargs.get("cart_uuid")
        try:
            cart = Cart.objects.get(uuid=cart_id)
        except Cart.DoesNotExist:
            raise NotFound('A cart with this id does not exist')
        return self.queryset.filter(cart=cart)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = self.kwargs.get("cart_uuid")
        cart, cart_item = CartService.add_to_cart(**serializer.validated_data, cart_id=id)
        return Response({'payload': self.get_serializer(cart_item, many=True).data}, status=status.HTTP_200_OK)

    # def create(self, *args, **kwargs):
