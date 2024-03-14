from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=200, required=True)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1','password2']
