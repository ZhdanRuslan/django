from django.shortcuts import render
from .models import Phone, Laptop
# Create your views here.


def index(request):
    context = dict()
    all_phones = Phone.objects.all()
    all_laptops = Laptop.objects.all()
    context['all_phones'] = all_phones
    context['all_laptops'] = all_laptops
    return render(request, 'product/index.html', context)




def detail_view(request, pk):
    phone = Phone.objects.get(id=pk)
    laptop = Laptop.objects.get(id=pk)
    ctx = {
        'phone_instance': phone,
        'laptop_instance': laptop

    }

    return render(request, 'product/detail_view.html', ctx)

