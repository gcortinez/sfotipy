from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.contrib.auth import login
# Create your views here.

def signup(request):
    form = UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, 'signup.html', {'forms' : form})


def signin(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        login(request, form.get_user())

    return render(request, 'signin.html', {'form': form})