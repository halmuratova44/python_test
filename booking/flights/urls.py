from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='default_flight_list'),  # Маршрут по умолчанию /flights/
    path('list/', views.flight_list, name='flight_list'),     # Список рейсов
    path('add/', views.add_flight, name='add_flight'),        # Добавление рейса
    path('delete/<int:pk>/', views.delete_flight, name='delete_flight'),  # Удаление рейса
    path('edit/<int:pk>/', views.edit_flight, name='edit_flight'),        # Редактирование рейса
    path('search/', views.search_flights, name='search_flights'),        # Поиск рейсов
    path('booking_success/<int:flight_id>/', views.booking_success, name='booking_success'),  # Успешное бронирование
    path('select_flight/<int:flight_id>/', views.select_flight, name='select_flight'),        # Выбор рейса
    path('payment/success/', views.payment_process, name='payment_success'),  # Оплата
    path('payment_process/<int:flight_id>/', views.payment_process, name='payment_process'),
    path('payment_confirmation/<int:flight_id>/', views.payment_confirmation, name='payment_confirmation'),
    path('booking/confirmation/<int:flight_id>/', views.booking_confirmation, name='booking_confirmation'),  # Подтверждение бронирования
]
