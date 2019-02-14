from django.urls import path
from .views import index, update_vacancies

urlpatterns = [
    path('', index),
    path('update/', update_vacancies),
]
