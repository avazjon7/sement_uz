from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sement_uz import views
from sement_uz.views import sales_statistics

# Create a router for the API viewsets
router = DefaultRouter()
router.register(r'api/products', views.ProductViewSet)
router.register(r'api/users', views.UserViewSet)
router.register(r'api/orders', views.OrderViewSet)

urlpatterns = [
    # DRF API URLs
    path('', include(router.urls)),
    path('sales-statistics/', sales_statistics, name='sales_statistics'),# This will include all the API routes from the router
]
