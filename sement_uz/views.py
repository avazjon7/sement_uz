from rest_framework import viewsets
from rest_framework.response import Response
from sement_uz.models import Product, Order, User, Payment
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import Product
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import PaymentForm
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY


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


def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = int(form.cleaned_data['amount'] * 100)  # Stripe accept sum in cents
            token = form.cleaned_data['stripeToken']

            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    source=token,
                    description='Example charge'
                )

                Payment.objects.create(
                    user=request.user,
                    amount=form.cleaned_data['amount'],
                    stripe_charge_id=charge.id
                )

                messages.success(request, "Payment has been successfuly!")
                return redirect('payment_success')
            except stripe.error.StripeError:
                messages.error(request, "Error in payment.")
                return redirect('payment_failed')

    else:
        form = PaymentForm()

    return render(request, 'sement_uz/payment.html',
    {'form': form, 'pk_test_51Q7cnmL8jnOjslxdyoO4jZGqcFuQkRs1Xvou05sY9ZaJfb9513CMsVf0EMveVRhZPqqzC9ZoYRiLfFF0dRp3giaR00BlvWOQMc':
    settings.STRIPE_PUBLISHABLE_KEY})
