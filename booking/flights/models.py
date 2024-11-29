from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)  # Номер рейса
    departure_city = models.CharField(max_length=100)  # Город отправления
    arrival_city = models.CharField(max_length=100)  # Город назначения
    departure_time = models.DateTimeField()  # Время отправления
    arrival_time = models.DateTimeField()  # Время прибытия
    airline = models.CharField(max_length=100)  # Авиакомпания
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена билета
    seats_available = models.PositiveIntegerField()  # Количество доступных мест
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания рейса
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления рейса

    def __str__(self):
        return f"{self.flight_number} from {self.departure_city} to {self.arrival_city}"


class Booking(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Мужчина'), ('F', 'Женщина')])
    birth_date = models.DateField()
    document_type = models.CharField(max_length=100)
    document_number = models.CharField(max_length=100)
    document_expiry = models.DateField()
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


