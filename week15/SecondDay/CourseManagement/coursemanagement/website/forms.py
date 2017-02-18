from django import forms
from .models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(label="Enter email")
    password = forms.CharField(label="Enter password",
                               widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20, label="Enter first name")
    last_name = forms.CharField(max_length=20, label="Enter last name")

    def save(self, commit=True):
        user = User.objects.create(email=self.cleaned_data['email'],
                                   password=self.cleaned_data['password'],
                                   first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'])

        user.save()

        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter email")
    password = forms.CharField(label="Enter password",
                               widget=forms.PasswordInput)

    def save(self, commit=True):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        return User.login(email, password)
