# from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from . import views

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
#
# urlpatterns = [
#     path('my-cart/<int:pk>/', views.CartView.as_view()),
#     # path('my-cart/<int:cart_pk>/items/', views.CartItemsView.as_view()),
#     # path('my-cart/<int:cart_pk>/items/<int:pk>', views.CartItemsView.as_view()),
#     # path('products/<int:pk>/', views.ProductDetailView.as_view()),
#     # path('categories/', views.CategoryList.as_view()),
#     # path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
#     # path('store/', include('store.urls')),
#     # path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

router = SimpleRouter()
router.register('my-cart', views.CartView)

book_router = routers.NestedSimpleRouter(
    router,
    r'my-cart',
    lookup='cart')

book_router.register(
    r'items',
    views.CartItemsView,
)
app_name = 'cart'

urlpatterns = [
    path('cart/', views.CartIdRequestView.as_view()),
    path('v2/my-cart/<uuid:id>', views.CartViewV2.as_view())
]

urlpatterns += [
    path('', include(router.urls)),
    path('', include(book_router.urls)),
]
