from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sement_uz.models import Product,User

# Register your models here.

admin.site.register(Product)
admin.site.register(User)

