from django import forms

from .models import TestFormModel


class TestForm(forms.ModelForm):
    class Meta:
        model = TestFormModel
        fields = '__all__'
