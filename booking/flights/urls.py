# flights/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.flight_list, name='flight_list'),  # Теперь он будет доступен по /list/
    path('add/', views.add_flight, name='add_flight'),
    path('delete/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('edit/<int:pk>/', views.edit_flight, name='edit_flight'),
    path('search/', views.search_flights, name='search_flights'),
]


