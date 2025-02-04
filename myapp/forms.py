from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username', "password1", 'password2', 'email']


class LoginForm(AuthenticationForm):
    class Meta:
        username=forms.CharField(max_length=150, label="USERNAME")
        password=forms.CharField(max_length=150, label="PASSWORD",widget=forms.PasswordInput)