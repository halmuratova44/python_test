# forms.py
from django import forms
from .models import Flight
from .models import Booking

# forms.py
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'gender',
            'birth_date',
            'document_type',
            'document_number',
            'document_expiry',  # Поле для даты окончания документа
            'phone_number',  # Поле для телефона
        ]
        widgets = {
            'birth_date': forms.SelectDateWidget(years=range(1900, 2025)),
            'document_expiry': forms.SelectDateWidget(years=range(2024, 2050)),
            'phone_number': forms.TextInput(attrs={'placeholder': '+996 700 000 000'})
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Валидация номера телефона
        if not phone_number.startswith("+996"):
            raise forms.ValidationError("Номер телефона должен начинаться с +996.")
        if len(phone_number) != 13:
            raise forms.ValidationError("Номер телефона должен быть 13 символов.")
        if not phone_number[1:].isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time', 'airline', 'price', 'seats_available']
