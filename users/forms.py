from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'username', 'placeholder':"Your Name"}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'placeholder': "Your Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'subject', 'placeholder': "Your Password"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'message', 'placeholder': "Confirm Your Password"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'name', 'placeholder': "Your Name"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'subject', 'placeholder': "Your Password"}))
