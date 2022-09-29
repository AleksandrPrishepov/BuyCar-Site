from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from car.models import *

class AddCarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_published'].initial = True
        self.fields['cat_car_model'].empty_label = 'Модель не выбрана'
        self.fields['cat_car_brand'].empty_label = 'Марка не выбрана'

    class Meta:
        model = OwnerAuto
        fields = '__all__'
        exclude = ['time_create', 'time_update']
        widjet = {
            'description':forms.Textarea(attrs={'cols':60,'rows':30}),
            'brand_owner':forms.TextInput(attrs={'class':'form-input'}),
            'model_owner':forms.TextInput(attrs={'class':'form-input'}),
            'name_owner':forms.TextInput(attrs={'class':'form-input'})
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))