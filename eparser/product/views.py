from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View, generic

from .models import Vacancy
from .main import start_app
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Index(View):
    template_name = 'product/index.html'
    context = dict()

    @method_decorator(login_required, settings.LOGIN_URL)
    def get(self, request):
        if request.GET.get('parse_btn') == 'Parse':
            start_app()
            return redirect(settings.LOGIN_REDIRECT_URL)
        if request.GET.get('logout_btn') == 'Logout':
            logout(request)
            return redirect(settings.LOGIN_URL)
        if request.GET.get('delete_btn') == 'Delete':
            Vacancy.objects.all().delete()
            return redirect(settings.LOGIN_REDIRECT_URL)
        all_vacancies = Vacancy.objects.all()
        self.context['all_vacancies'] = all_vacancies
        return render(request, self.template_name, self.context)


class RegisterNewUser(generic.CreateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'registration/register.html')

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('username')
        pwd = self.request.POST.get('password')
        email = self.request.POST.get('email')

        User.objects.create_user(username=name, email=email, password=pwd)
        return redirect('/')
