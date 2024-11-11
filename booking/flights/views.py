from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Flight


from .forms import FlightForm


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'add_flight.html', {'form': form})


def delete_flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'delete_flight.html', {'flight': flight})

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'flights': flights})

