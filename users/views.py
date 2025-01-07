from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUserModel
from .utils import send_email_confirmation


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email is confirmed
            user.save()
            send_email_confirmation(user, request)
            messages.success(request, "A confirmation email has been sent to your email address.")
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def email_confirm_view(request, uid, token):
    try:
        user = CustomUserModel.objects.get(pk=uid)
    except CustomUserModel.DoesNotExist:
        return HttpResponse("Invalid confirmation link.", status=400)

    if default_token_generator.check_token(user, token):
        user.is_active = True  # Activate the user
        user.save()
        return redirect('users:login')
    else:
        return HttpResponse("Invalid or expired token.", status=400)


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('/')  # Replace 'home' with your desired URL name
            else:
                form.add_error(None, "Invalid email/username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})
