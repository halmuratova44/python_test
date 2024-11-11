from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('airline.urls')),  # Подключаем URL из приложения airline
]
