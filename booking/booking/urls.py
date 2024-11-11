from django.contrib import admin
from django.urls import path, include
from flights import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('airline.urls')),  # Заменено на airline
    path('admin/', admin.site.urls),
    path('', include('airline.urls')),
    path('flights/', include('flights.urls'))
]



