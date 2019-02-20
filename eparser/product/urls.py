from django.urls import path, include

from .views import Index, RegisterNewUser

urlpatterns = [
    path('register/', RegisterNewUser.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', Index.as_view(), name='index'),
]
