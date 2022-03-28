from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from account.permissions import IsCustomer, IsSellerOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ProductList(generics.ListCreateAPIView):
    # permission_classes = [IsSellerOrReadOnly]
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    # filter_backends = [DjangoFilterBackend]

    # TODO: override search to create more advanced search
    filterset_fields = ['category', 'price']
    search_fields = ['title', 'category__name', ]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user.seller)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsCustomer]
    # print('request.user')
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
