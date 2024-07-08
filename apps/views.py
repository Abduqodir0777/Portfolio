from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login

from apps.models import User
from apps.forms import SignUpForm


def homepagefunc(request):
    return render(request, 'main.html')


def index(request):
    return render(request, 'index.html')


def signupfunc(request):
    if request.method == 'POST':
        data = SignUpForm(request.POST, files=request.FILES)
        if data.is_valid():
            user = data.save()
            login(request, user)
            return redirect('login')
        else:
            print(data.errors)
            return render(request, 'signup.html', {'form': data})
    else:
        data = SignUpForm()
    return render(request, 'signup.html', {'form': data})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return redirect('my-profile')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})
    return render(request, 'login.html')


def userfunc(request, username):
    users = User.objects.filter(username=username).first()
    if users:
        return render(request, 'index.html', {'users': users, 'username': username})
    else:
        return HttpResponse('<h1 style="text-align: center; margin-top: 200px;">404 - Page Not Found!</h1>')
