from rest_framework import viewsets
from rest_framework.response import Response
from sement_uz.models import Product, Order, User
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# API View for Product List and Detail
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

# API View for User List and Detail
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# API View for Order List and Detail
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def sales_statistics(request):
    # Aggregate the total quantity sold for each product
    product_sales = Order.objects.values('product__name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')

    context = {
        'product_sales': product_sales
    }
    return render(request, 'sement_uz/admin/sales_statistics.html', context)



@login_required
def my_view(request):
    return render(request, 'your_template.html')  #protecdet code

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'sement_uz/product_list.html', {'products': products})