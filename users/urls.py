from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import register_view, login_view, email_confirm_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),  # User registration
    path('login/', login_view, name='login'),  # User login
    path('logout/', LogoutView.as_view(), name='logout'),  # User logout
    path('confirm/<int:uid>/<str:token>/', email_confirm_view, name='email_confirm'),  # Email confirmation
]
