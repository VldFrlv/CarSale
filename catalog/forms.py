from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type_of_venc', 'brand', 'model', 'fuel', 'engine_volume','drive',
                  'year', 'color', 'price', 'price_currency', 'mileage', 'description',
                  'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']

