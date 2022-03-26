# from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    # APIs v1
    path('v1/register/', views.CustomerViews.as_view()),
    path('v1/guest-token/', views.CustomerDataViews.as_view()),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('products/<int:pk>/', views.ProductDetailView.as_view()),
    # path('categories/', views.CategoryList.as_view()),
    # path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
    # path('store/', include('store.urls')),
    # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
