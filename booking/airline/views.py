from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import UserLoginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from flights.models import Flight


def home(request):
    flights = Flight.objects.all()
    return render(request, 'airline/home.html', {'flights': flights})








def login_view(request):
    """Обработка входа пользователя."""
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in!')
                return redirect('home')  # Перенаправление на главную страницу
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'airline/login.html', {'form': form})


def register(request):
    """Обработка регистрации нового пользователя."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт успешно создан для {username}!')
            return render(request, 'airline/home.html', {'form': form}) # Перенаправление на страницу входа
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, проверьте данные.')
    else:
        form = UserRegisterForm()

    return render(request, 'airline/register.html', {'form': form})