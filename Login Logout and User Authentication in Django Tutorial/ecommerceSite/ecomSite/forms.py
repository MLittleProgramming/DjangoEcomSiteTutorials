from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Provide a valid email address.')
    date_of_birth = forms.DateField(initial=datetime.date.today, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth', 'password1', 'password2')
