from django import forms
from django.contrib.auth.models import User
from lists.models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ),
        help_text='Пароль: '
    )

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ivan-ivanov'
        }
    ),
        help_text='Имя пользователя:'
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ivan-ivanov@mail.ru'
        }
    ),
        help_text='E-mail: '
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class TypeForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Predator'
        }
    ),
        max_length=128,
        help_text='Пожалуйста введите название типа корабля: ')

    class Meta:
        model = Type
        fields = ('type', )


class SeriesForm(forms.ModelForm):
    series = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Super'
        }
    ),
        max_length=128,
        help_text='Пожалуйста, введите название серии корабля: ')

    class Meta:
        model = Series
        fields = ('series', )


class ShipForm(forms.ModelForm):
    type = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ),
        queryset=Type.objects.all(),
        help_text='Выберите тип: ',)

    series = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ),
        queryset=Series.objects.all(),
        help_text='Выберите серию: ')

    lenght = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ),
        help_text='Введите длину: ',
        min_value=1)

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ANTI-MUSOR'
        }
    ), max_length=128, help_text='Введите название корабля: ')

    side = forms.ModelChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ),
        queryset=Side.objects.all(),
        help_text='Выберите сторону: ')

    class Meta:
        model = Ship
        exclude = ()

