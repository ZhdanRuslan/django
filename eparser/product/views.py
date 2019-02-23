from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View

from .models import Vacancy
from .parsers_settings import REQUEST_URL, BASE_URL, CITY_DICT, CITY
from .main import start_app
from django.conf import settings


class Index(View):
    template_name = 'product/main.html'
    context = dict()

    def get(self, request):
        if request.GET.get('parse_btn') == 'Parse':
            start_app(REQUEST_URL)
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
        request_url = BASE_URL + spec + CITY_DICT.get(CITY) + '/pg'
        start_app(request_url)
        return redirect(settings.LOGIN_REDIRECT_URL)
