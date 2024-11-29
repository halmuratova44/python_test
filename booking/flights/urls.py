# flights/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.flight_list, name='flight_list'),  # Теперь он будет доступен по /list/
    path('add/', views.add_flight, name='add_flight'),
    path('delete/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('edit/<int:pk>/', views.edit_flight, name='edit_flight'),
    path('search/', views.search_flights, name='search_flights'),
    path('booking_success/<int:flight_id>/', views.booking_success, name='booking_success'),
    path('select_flight/<int:flight_id>/', views.select_flight, name='select_flight'),
    path('payment/success/', views.payment_process, name='payment_success'),
    path('booking/confirmation/<int:flight_id>/', views.booking_confirmation, name='booking_confirmation'),
]


