from django.db.models import Q
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from apps.models import User
from apps.forms import SignUpForm


def homepagefunc(request):
    return render(request, 'main.html')


def signupfunc(request):
    if request.method == 'POST':
        data = SignUpForm(request.POST, files=request.FILES)
        if data.is_valid():
            user = data.save(commit=False)
            user.password = make_password(data.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')
        else:
            print(data.errors)
            return render(request, 'signup.html', {'form': data})
    else:
        data = SignUpForm()
    return render(request, 'signup.html', {'form': data})


def loginfunc(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('my-profile')
    return render(request, 'login.html')


# @login_required
def index(request):
    return render(request, 'index.html')


def userfunc(request, username):
    users = User.objects.filter(username=username).first()
    if users:
        return render(request, 'index.html', {'users': users, 'username': username})
    else:
        return HttpResponse('<h1 style="text-align: center; margin-top: 200px;">404 - Page Not Found!</h1>')
