import asyncio

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings

from .models import Vacancy
from .parsers_settings import REQUEST_URL, BASE_URL, CITY_DICT, SPECIALIZATION_DICT
from .main import start_app


class Index(View):
    template_name = 'product/main.html'
    context = dict()

    def get(self, request):
        if request.GET.get('parse_btn') == 'Parse':
            self.context['city'] = 'Ukraine'
            asyncio.run(start_app(REQUEST_URL))
            return redirect(settings.LOGIN_REDIRECT_URL)
        if request.GET.get('logout_btn') == 'Logout':
            logout(request)
            return redirect(settings.LOGIN_REDIRECT_URL)
        if request.GET.get('delete_btn') == 'Delete':
            Vacancy.objects.all().delete()
            return redirect(settings.LOGIN_REDIRECT_URL)
        all_vacancies = Vacancy.objects.all()
        self.context['all_vacancies'] = all_vacancies
        return render(request, self.template_name, self.context)

    def post(self, request):
        spec = request.POST.get('profession')
        city = request.POST.get('city')
        request_url = BASE_URL + str(SPECIALIZATION_DICT.get(spec)) + str(CITY_DICT.get(city))
        asyncio.run(start_app(request_url))
        return redirect(settings.LOGIN_REDIRECT_URL)
