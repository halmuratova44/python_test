from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from decimal import Decimal
from .models import Flight, Booking
from .forms import FlightForm, BookingForm


# Функция для отображения списка рейсов
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})


# Поиск рейсов
def search_flights(request):
    flights = Flight.objects.all()

    departure_city = request.GET.get('departure_city', '').strip()
    arrival_city = request.GET.get('arrival_city', '').strip()
    departure_date = request.GET.get('departure_date', '').strip()
    ticket_class = request.GET.get('ticket_class', '').strip()

    # Фильтрация по городу отправления
    if departure_city:
        flights = flights.filter(departure_city__icontains=departure_city)

    # Фильтрация по городу назначения
    if arrival_city:
        flights = flights.filter(arrival_city__icontains=arrival_city)

    # Фильтрация по дате отправления
    if departure_date:
        flights = flights.filter(departure_time__date=departure_date)

    # Фильтрация по классу билета и наличию мест
    if ticket_class:
        if ticket_class == 'BUSINESS':
            flights = flights.filter(business_seats__gt=0)  # Проверяем, что есть свободные места в бизнес-классе
        elif ticket_class == 'COMFORT':
            flights = flights.filter(comfort_seats__gt=0)  # Проверяем, что есть свободные места в комфорт-классе
        elif ticket_class == 'ECONOMY':
            flights = flights.filter(economy_seats__gt=0)  # Проверяем, что есть свободные места в эконом-классе

    return render(request, 'flights/search_flights.html', {'flights': flights})


# Вспомогательная функция для расчета цены билета
def calculate_ticket_price(base_price, ticket_class):
    if ticket_class == 'BUSINESS':
        return base_price * Decimal('2.0')
    elif ticket_class == 'COMFORT':
        return base_price * Decimal('1.5')
    return base_price


# Добавление нового рейса
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save()
            base_price = flight.price
            business_seats = flight.business_seats
            comfort_seats = flight.comfort_seats
            economy_seats = flight.economy_seats

            # Создаем билеты для каждого класса
            for ticket_class in [('BUSINESS', business_seats),
                                            ('COMFORT', comfort_seats),
                                            ('ECONOMY', economy_seats)]:
                price = calculate_ticket_price(base_price, ticket_class)
                for _ in range(10):  # Просто пример для создания 10 билетов
                    Booking.objects.create(
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
                    )
            return redirect('flight_list')
    else:
        form = FlightForm()

    return render(request, 'flights/add_flight.html', {'form': form})


# Редактирование рейса
def edit_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)

    return render(request, 'flights/edit_flight.html', {'form': form, 'flight': flight})


# Удаление рейса
def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flights/delete_flight.html', {'flight': flight})







def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'flights/booking_success.html', {'booking': booking})



# Выбор рейса
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm
from decimal import Decimal

# Выбор рейса
def select_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    economy_seats = flight.economy_seats
    comfort_seats = flight.comfort_seats
    business_seats = flight.business_seats

    economy_class_price = flight.price
    comfort_class_price = economy_class_price * Decimal('1.30')  # 30% выше
    business_class_price = economy_class_price * Decimal('2')  # В 2 раза выше

    context = {
        'flight': flight,
        'economy_seats': economy_seats,
        'comfort_seats': comfort_seats,
        'business_seats': business_seats,
        'economy_class_price': economy_class_price,
        'comfort_class_price': comfort_class_price,
        'business_class_price': business_class_price,
    }

    return render(request, 'flights/select_flight.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm

# Подтверждение бронирования
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm

# Подтверждение бронирования
from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm

def booking_confirmation(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    # Получаем выбранный класс билета из GET-запроса
    selected_class = request.GET.get('ticket_class')

    # Проверка на наличие выбранного класса
    if not selected_class:
        return render(request, 'flights/booking_confirmation.html', {
            'flight': flight,
            'error': 'Ошибка: Класс билета не выбран.',
        })

    # Проверка доступных мест в выбранном классе
    if selected_class == 'BUSINESS' and flight.business_seats <= 0:
        return render(request, 'flights/booking_confirmation.html', {
            'flight': flight,
            'selected_class': selected_class,
            'error': 'Ошибка: Нет доступных мест в бизнес классе.',
        })
    elif selected_class == 'COMFORT' and flight.comfort_seats <= 0:
        return render(request, 'flights/booking_confirmation.html', {
            'flight': flight,
            'selected_class': selected_class,
            'error': 'Ошибка: Нет доступных мест в комфорт классе.',
        })
    elif selected_class == 'ECONOMY' and flight.economy_seats <= 0:
        return render(request, 'flights/booking_confirmation.html', {
            'flight': flight,
            'selected_class': selected_class,
            'error': 'Ошибка: Нет доступных мест в эконом классе.',
        })

    # Обработка формы при отправке POST-запроса
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            # Сохраняем бронирование
            booking = form.save(commit=False)
            booking.flight = flight
            booking.ticket_class = selected_class  # Сохраняем выбранный класс
            booking.save()

            # Уменьшаем количество мест в зависимости от выбранного класса
            flight.reduce_seat_count(selected_class)

            # Перенаправляем пользователя на страницу оплаты
            return redirect('payment_process', flight_id=flight.id)

    else:
        # Если форма еще не отправлялась, передаем выбранный класс как скрытое поле
        form = BookingForm(initial={'ticket_class': selected_class})

    return render(request, 'flights/booking_confirmation.html', {
        'flight': flight,
        'form': form,
        'selected_class': selected_class,
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking

def payment_process(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    ticket_class = request.POST.get('ticket_class')

    if request.method == 'POST':
        # Получаем данные карты
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Проверка, что все поля заполнены
        if card_number and expiry_date and cvv:
            # Уменьшаем количество мест в зависимости от выбранного класса билета
            flight.reduce_seat_count(ticket_class)

            # Переход на страницу подтверждения платежа
            return redirect('payment_confirmation', flight_id=flight.id)

        return render(request, 'flights/payment_process.html', {
            'flight': flight,
            'ticket_class': ticket_class,
            'error': 'Ошибка: Проверьте данные карты.'
        })

    return render(request, 'flights/payment_process.html', {'flight': flight, 'ticket_class': ticket_class})

def payment_confirmation(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, 'flights/payment_confirmation.html', {'flight': flight})

