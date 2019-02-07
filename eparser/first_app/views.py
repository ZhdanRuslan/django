from django.shortcuts import render

def index(request):
    context = {}
    context['key'] = 'value'
    context['four'] = 2 + 2
    return render(request, 'index.html', context)


def main(request):
    context = {}
    return render(request, 'main.html', context)