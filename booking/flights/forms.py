# forms.py
from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'airline', 'price', 'seats_available']
