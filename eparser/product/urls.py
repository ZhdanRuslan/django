from django.urls import path, include
from .views import Index

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index.as_view(), name='index'),
]
