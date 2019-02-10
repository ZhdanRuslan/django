from django.shortcuts import render
from .models import Phone
# Create your views here.


def index(request):
    context = dict()
    all_phones = Phone.objects.all()
    context['all_phones'] = all_phones
    return render(request, 'product/index.html', context)




def detail_view(request, pk):
    phone = Phone.objects.get(id=pk)
    ctx = {
        'phone_instance': phone
    }

    return render(request, 'product/detail_view.html', ctx)

