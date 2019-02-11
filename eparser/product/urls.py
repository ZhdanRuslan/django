from django.urls import path
from .views import index, detail_view

urlpatterns = [
    path('', index),
    path('detail-view/<int:pk>', detail_view)
]
