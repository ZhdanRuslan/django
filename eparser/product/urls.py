from django.urls import path, include
from .views import index, update_vacancies

urlpatterns = [
    path('', index),
    path('update/', update_vacancies),
    path('accounts/', include('django.contrib.auth.urls')),
]
