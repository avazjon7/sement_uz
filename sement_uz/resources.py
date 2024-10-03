from import_export import resources
from .models import Product, User, Order


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
