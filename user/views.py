from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, ("Incorrect logins"))
            return redirect('index')
    else:
        return render(request, 'user/index.html')

def userRegistration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('profile')
    else:
        form = UserCreationForm()
    
    return render(request, 'user/userRegistration.html', {'form': form})