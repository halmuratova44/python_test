from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('airline.urls')),  # Заменено на airline
    path('flights/', include('flights.urls'))
=======
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('airline.urls')),  # Подключаем URL из приложения airline
>>>>>>> origin/master
]
