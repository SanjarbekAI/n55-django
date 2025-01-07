# forms.py
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


# forms.py
from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(forms.Form):
    username = forms.CharField(
        label=_("Email or Username"),
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email or Username'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    _("Invalid email/username or password.")
                )
        return cleaned_data
