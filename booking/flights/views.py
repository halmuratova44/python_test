from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Flight


from .forms import FlightForm

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Flight
from .models import Booking
from .forms import BookingForm



def payment_process(request):
    if request.method == 'POST':
        # Получаем данные с формы
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        # Здесь можно добавить логику для обработки платежа
        # Например, отправка данных в платежную систему (Stripe, PayPal, и т.д.)

        # После успешной оплаты можно выполнить редирект на страницу подтверждения оплаты
        return redirect('payment_confirmation')  # Переход на страницу подтверждения оплаты
    else:
        return redirect('booking_success')

def booking_success(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight  # Привязываем бронирование к рейсу
            booking.save()  # Сохраняем бронирование в базе данных
            return redirect('booking_confirmation', flight_id=flight.id)  # Перенаправляем на страницу подтверждения
    else:
        form = BookingForm()

    return render(request, 'flights/booking_success.html', {'flight': flight, 'form': form})

def booking_confirmation(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)

    return render(request, 'flights/booking_confirmation.html', {'flight': flight})

def select_flight(request, flight_id):
    # Получаем рейс по ID или возвращаем ошибку 404, если рейс не найден
    flight = get_object_or_404(Flight, pk=flight_id)

    # Передаем данные рейса в контекст шаблона
    return render(request, 'flights/select_flight.html', {'flight': flight})

def search_flights(request):
    flights = Flight.objects.all()


    departure_city = request.GET.get('departure_city', '').strip()
    arrival_city = request.GET.get('arrival_city', '').strip()
    departure_date = request.GET.get('departure_date', '').strip()


    if departure_city:
        flights = flights.filter(departure_city__icontains=departure_city)
    if arrival_city:
        flights = flights.filter(arrival_city__icontains=arrival_city)
    if departure_date:
        flights = flights.filter(departure_time__date=departure_date)

    return render(request, 'flights/search_flights.html', {'flights': flights})


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/add_flight.html', {'form': form})


def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flights/delete_flight.html', {'flight': flight})

def edit_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)  # Получаем рейс по pk
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)  # Загружаем данные рейса в форму для редактирования
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('flight_list')  # Перенаправление на страницу со списком рейсов
    else:
        form = FlightForm(instance=flight)  # Заполняем форму существующими данными рейса
    return render(request, 'flights/edit_flight.html', {'form': form, 'flight': flight})

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

