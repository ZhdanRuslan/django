from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = dict()
    context['key'] = 'value'
    context['four'] = 2 + 2
    return render(request, 'first_app/index.html', context)


def main(request):
    context = dict()
    return render(request, 'first_app/main.html', context)


def testref(request):
    return HttpResponse('Test ref works correct!')