from django.urls import path, include
from sement_uz import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from config import settings



router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [

    path('api/', include(router.urls)),

    # Regular views
    path('sales-statistics/', views.sales_statistics, name='sales_statistics'),
    path('my-view/', views.my_view, name='my_view'),
    path('product-list/', views.product_list, name='product_list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
