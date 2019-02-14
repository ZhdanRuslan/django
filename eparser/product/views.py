from django.shortcuts import render
from .models import Phone, Laptop, Order, Vacancy
from .main import start_app


def index(request):
    context = dict()
    all_phones = Phone.objects.all()
    all_laptops = Laptop.objects.all()
    all_orders = Order.objects.all()
    all_vacancies = Vacancy.objects.all()
    context['all_phones'] = all_phones
    context['all_laptops'] = all_laptops
    context['all_orders'] = all_orders
    context['all_vacancies'] = all_vacancies
    return render(request, 'product/index.html', context)


def detail_view(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    ctx = {
        'vacancy_instance': vacancy,
    }

    return render(request, 'product/detail_view.html', ctx)


def update_vacancies(request):
    start_app()
