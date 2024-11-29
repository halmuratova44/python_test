from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate
from flights.models import Flight

def home(request):
    """Главная страница с рейсами."""
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

                # Перенаправление на страницу, куда пользователь пытался попасть до входа
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
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

            # Перенаправляем на страницу входа, после успешной регистрации
            return redirect('login')
        else:
            messages.error(request, 'Ошибка при регистрации. Пожалуйста, проверьте данные.')
    else:
        form = UserRegisterForm()

    return render(request, 'airline/register.html', {'form': form})
