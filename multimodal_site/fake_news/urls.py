from django.urls import path
from .views import (
    index, register, login, home,
    training, predict, history,
    logout, admin_login, admin_dashboard,
    toggle_user_status, admin_logout
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('training/', training, name='training'),
    path('predict/', predict, name='predict'),
    path('history/', history, name='history'),
    path('logout/', logout, name='logout'),

    path('admin-login/', admin_login, name='admin_login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('toggle-user/<int:user_id>/', toggle_user_status, name='toggle_user'),
    path('admin-logout/', admin_logout, name='admin_logout'),
]