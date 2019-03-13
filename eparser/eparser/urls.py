from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-action/', include('user_app.urls')),
    path('api-vacancy/', include('rest.urls')),
    path('', include('product.urls')),
]
