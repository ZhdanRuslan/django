from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path('main/', views.main),
    path('testref/', views.testref)
]
