from django import forms

from .models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name']
        labels = {
            'email': 'Enter email',
            'password': 'Enter password',
            'first_name': 'Enter first name',
            'last_name': 'Enter last name'
        }
        widgets = {
            'password': forms.PasswordInput()
        }
