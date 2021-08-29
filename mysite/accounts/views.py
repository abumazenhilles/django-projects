from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Correct the errors below')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

def dashboard_view(request):
	return render(request, 'dashboard.html')

def index_view(request):
	return render(request, 'index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Username or Password Incorrect")
            return render(request, "login.html", context)

        messages.success(request, "You have successfully logged in.")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "please logout")
    return redirect("index")
