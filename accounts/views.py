from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

# Password: #HuegN9fiYMXef#

def register_view(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):

    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Password changed successfully!")
            login(request, user)

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'profile.html', {'user': request.user, 'form': form})
