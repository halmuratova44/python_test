from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('register/', views.register, name='register'),  # Страница регистрации
    path('login/', views.login_view, name='login'),  # Страница входа
]
