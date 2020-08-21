from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import SiteUsers


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            date_of_birth = form.cleaned_data.get('date_of_birth')
            SiteUsers.objects.create(user=user, date_of_birth=date_of_birth)
            login(request, user)
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, 'signup.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form', form})


