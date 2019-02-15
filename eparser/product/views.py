from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from .main import start_app


class Index(View):
    template_name = 'product/index.html'
    context = dict()

    def get(self, request):

        if request.user.is_authenticated:
            if request.GET.get('mybtn') == 'START':
                start_app()
            all_vacancies = Vacancy.objects.all()
            self.context['all_vacancies'] = all_vacancies
            return render(request, self.template_name, self.context)
        else:
            return redirect('accounts/login/')

