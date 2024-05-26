from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs', 'placeholder': 'Name', 'value':''}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'inputs', 'placeholder': 'Email','value':''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputs', 'placeholder': 'Password','value':''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'inputs', 'placeholder': 'Conform Password','value':''}))

    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']