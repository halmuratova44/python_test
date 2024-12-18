from django import forms
from .models import Flight, Booking

# Форма бронирования
class BookingForm(forms.ModelForm):
    ticket_class = forms.CharField(widget=forms.HiddenInput())  # Скрытое поле для класса билета

    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'gender', 'birth_date', 'document_type',
            'document_number', 'document_expiry', 'phone_number', 'ticket_class',
        ]
        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1900, 2025)),
            'document_expiry': forms.SelectDateWidget(years=range(2024, 2050)),
            'phone_number': forms.TextInput(attrs={'placeholder': '+996 700 000 000'})
        }


# Форма рейса
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = [
            'flight_number',  # Номер рейса
            'departure_city',  # Город отправления
            'arrival_city',  # Город назначения
            'departure_time',  # Время отправления
            'arrival_time',  # Время прибытия
            'airline',  # Авиакомпания
            'price',  # Цена
            'seats_available',  # Доступные места
            'business_seats',
            'comfort_seats',
            'economy_seats'
        ]
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Удобный ввод времени
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Удобный ввод времени
        }
