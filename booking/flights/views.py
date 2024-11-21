from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Flight


from .forms import FlightForm

from django.shortcuts import render
from .models import Flight

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

