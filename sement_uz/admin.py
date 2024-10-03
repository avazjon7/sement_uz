# sement_uz/admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLSX, CSV  # Import formats
from .models import Product, User, Order
from .resources import ProductResource, UserResource, OrderResource
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.db.models import Sum
from .models import Product, Order


def sales_statistics_view(request):
    product_sales = (
        Order.objects.values('product__name')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')
    )

    context = {
        'product_sales': product_sales
    }

    return TemplateResponse(request, 'sement_uz/admin/sales_statistics.html', context)

class CustomAdminSite(admin.AdminSite):
    site_header = 'My Admin Site'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('sales-statistics/', self.admin_view(sales_statistics_view), name='sales_statistics'),
        ]
        return custom_urls + urls

admin_site = CustomAdminSite(name='custom_admin')


class CustomImportExportModelAdmin(ImportExportModelAdmin):
    def get_export_formats(self):
        formats = super().get_export_formats()
        formats.append(XLSX)
        return formats

@admin.register(Product)
class ProductAdmin(CustomImportExportModelAdmin):
    resource_class = ProductResource

@admin.register(User)
class UserAdmin(CustomImportExportModelAdmin):
    resource_class = UserResource

@admin.register(Order)
class OrderAdmin(CustomImportExportModelAdmin):
    resource_class = OrderResource
