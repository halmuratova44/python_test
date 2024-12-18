from django.contrib import admin
from .models import Flight, Booking

# Inline для управления билетами
class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0  # Убираем пустые строки по умолчанию
    readonly_fields = ('ticket_class',)  # Делаем класс билета неизменяемым, если нужно

# Админка для модели Flight
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'price', 'seats_available')  # Какие поля показывать в списке
    search_fields = ('flight_number', 'departure_city', 'arrival_city')  # Поля для поиска
    inlines = [BookingInline]  # Связанные билеты
    actions = ['generate_tickets']  # Добавляем действие для генерации билетов

    @admin.action(description='Сгенерировать билеты для рейса')
    def generate_tickets(self, request, queryset):
        """Создаем билеты для всех классов"""
        for flight in queryset:
            base_price = flight.price
            tickets = []
            for ticket_class, multiplier in [(Flight.BUSINESS, 2.0), (Flight.COMFORT, 1.5), (Flight.ECONOMY, 1.0)]:
                for _ in range(10):  # Количество билетов каждого класса
                    tickets.append(Booking(
                        flight=flight,
                        ticket_class=ticket_class,
                        first_name="Имя",
                        last_name="Фамилия",
                        gender='M',
                        birth_date="2000-01-01",
                        document_type="Паспорт",
                        document_number="123456789",
                        document_expiry="2025-01-01",
                        phone_number="1234567890",
                    ))
            Booking.objects.bulk_create(tickets)  # Быстрая массовая вставка
        self.message_user(request, "Билеты успешно созданы.")

# Регистрируем модели в админке
admin.site.register(Flight, FlightAdmin)
admin.site.register(Booking)  # Регистрация модели Booking (если нужно)
