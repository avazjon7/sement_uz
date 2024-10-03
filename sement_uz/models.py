from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='product', null=True)
    quantity = models.IntegerField(default=0)

    @property
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None

class User(BaseModel):
    username = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='sement_uz/images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link order to a user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=13)
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='pending')  # Track order status

    def __str__(self):
        return f'{self.name} - {self.phone}'
