from django.shortcuts import render
from .models import Phone, Laptop, Order
from .main import start_app

# Create your views here.


def index(request):
    context = dict()
    start_app()
    all_phones = Phone.objects.all()
    all_laptops = Laptop.objects.all()
    all_orders = Order.objects.all()
    context['all_phones'] = all_phones
    context['all_laptops'] = all_laptops
    context['all_orders'] = all_orders
    return render(request, 'product/index.html', context)


def detail_view(request, pk):
    phone = Phone.objects.get(id=pk)
    laptop = Laptop.objects.get(id=pk)
    orders = Order.objects.get(id=pk)
    ctx = {
        'phone_instance': phone,
        'laptop_instance': laptop,
        'orders': orders
    }

    return render(request, 'product/detail_view.html', ctx)
