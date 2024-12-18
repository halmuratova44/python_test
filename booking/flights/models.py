from django.db import models

class Flight(models.Model):
    ECONOMY = 'Economy'
    COMFORT = 'Comfort'
    BUSINESS = 'Business'

    CLASS_CHOICES = [
        (ECONOMY, 'Эконом'),
        (COMFORT, 'Комфорт'),
        (BUSINESS, 'Бизнес'),
    ]

    flight_number = models.CharField(max_length=10, unique=True, verbose_name="Номер рейса")
    departure_city = models.CharField(max_length=100, verbose_name="Город отправления")
    arrival_city = models.CharField(max_length=100, verbose_name="Город назначения")
    departure_time = models.DateTimeField(verbose_name="Время отправления")
    arrival_time = models.DateTimeField(verbose_name="Время прибытия")
    airline = models.CharField(max_length=100, verbose_name="Авиакомпания")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    seats_available = models.PositiveIntegerField(verbose_name="Доступные места")
    business_seats = models.IntegerField(default=0)  # Количество мест в бизнес классе
    comfort_seats = models.IntegerField(default=0)  # Количество мест в комфорт классе
    economy_seats = models.IntegerField(default=0)  # Количество мест в эконом классе
    ticket_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES,
        default=ECONOMY,
        verbose_name="Класс билета"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"{self.flight_number} ({self.departure_city} -> {self.arrival_city})"

    def reduce_seat_count(self, ticket_class):
        """Метод для уменьшения количества мест в зависимости от класса билета."""
        if ticket_class == self.BUSINESS and self.business_seats > 0:
            self.business_seats -= 1
            print(f"Business seat reduced: {self.business_seats} left.")
        elif ticket_class == self.COMFORT and self.comfort_seats > 0:
            self.comfort_seats -= 1
            print(f"Comfort seat reduced: {self.comfort_seats} left.")
        elif ticket_class == self.ECONOMY and self.economy_seats > 0:
            self.economy_seats -= 1
            print(f"Economy seat reduced: {self.economy_seats} left.")

        # Обновляем общее количество доступных мест
        self.seats_available -= 1
        self.save()

        # Дополнительно можно выводить обновленные значения
        print(f"Total available seats: {self.seats_available}")


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="bookings", verbose_name="Рейс")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    gender = models.CharField(
        max_length=1,
        choices=[('M', 'Мужчина'), ('F', 'Женщина')],
        verbose_name="Пол"
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    document_type = models.CharField(max_length=100, verbose_name="Тип документа")
    document_number = models.CharField(max_length=100, verbose_name="Номер документа")
    document_expiry = models.DateField(verbose_name="Срок действия документа")
    phone_number = models.CharField(max_length=13, verbose_name="Номер телефона")
    ticket_class = models.CharField(
        max_length=10,
        choices=Flight.CLASS_CHOICES,
        default=Flight.ECONOMY,
        verbose_name="Класс билета"
    )

    def __str__(self):
        return f"Бронирование: {self.first_name} {self.last_name} на рейс {self.flight.flight_number}"
