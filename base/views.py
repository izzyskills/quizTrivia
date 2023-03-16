from django.shortcuts import render, redirect
from . import models, forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('register')

    return render(request, 'login.html')


def register_view(request):
    userForm = forms.UserCreationForm()
    profileForm = forms.ProfileCreationForm()
    context = {'userForm': userForm, 'profileForm': profileForm}
    if request.method == "POST":
        userForm = forms.UserCreationForm(request.POST)
        profileForm = forms.ProfileCreationForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.lower()
            user.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('login')
    return render(request, 'register.html', context)


@login_required(login_url='login')
def dashboard_view(request):
    user = User.objects.get(id=request.user.id)
    context = {'user': user}

    return render(request, 'dashboard.html', context)
