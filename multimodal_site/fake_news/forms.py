from django import forms
from .models import RegisteredUser

class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }