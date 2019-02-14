from django.shortcuts import render
from .models import Vacancy
from .main import start_app


def index(request):
    if request.GET.get('mybtn') == 'START':
        start_app()
    context = dict()
    all_vacancies = Vacancy.objects.all()
    context['all_vacancies'] = all_vacancies
    return render(request, 'product/index.html', context)


def detail_view(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    ctx = {
        'vacancy_instance': vacancy,
    }

    return render(request, 'product/detail_view.html', ctx)


def update_vacancies(request):
    context = dict()
    start_app()
    all_vacancies = Vacancy.objects.all()
    context['all_vacancies'] = all_vacancies
    return render(request, 'product/index.html', context)
