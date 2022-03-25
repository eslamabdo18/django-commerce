# from django.shortcuts import render
# from django.views import View
from rest_framework import generics, viewsets
from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
from cartapp.models import Cart, CartItem
from cartapp.serializers import CartSerializer, CartItemSerializer


class CartIdRequestView(generics.GenericAPIView):
    @swagger_auto_schema(responses={201: 'Created'})
    def get(self, request):
        if not request.session.get('cart_id'):
            print(request.session.get('cart_id'))
            cart = Cart.objects.create()
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


class CartItemsView(viewsets.ModelViewSet):
    # http_method_names = ['get']

    queryset = CartItem.objects.all().select_related('cart')
    # lookup_field = 'id'
    # lookup_field = 'uuid'

    serializer_class = CartItemSerializer

    def get_queryset(self, *args, **kwargs):
        cart_id = self.kwargs.get("cart_uuid")
        try:
            cart = Cart.objects.get(uuid=cart_id)
        except Cart.DoesNotExist:
            raise NotFound('A cart with this id does not exist')
        return self.queryset.filter(cart=cart)

    # def create(self, *args, **kwargs):
