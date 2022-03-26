# from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # print(request)
        if hasattr(request.user, 'customer'):
            return True
        return False


class IsSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # print(request.user)
        if request.method in SAFE_METHODS:
            return True

        if hasattr(request.user, 'seller'):
            print(request.user.seller)
            return True
        return False
