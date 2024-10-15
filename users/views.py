from dbm import error

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.forms import LoginForm, RegisterForm


def home(request):
    return render(request, 'users/home.html')


def loginHandler(request):

    form = LoginForm()
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'users/login.html', context)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            context = {'form': form, "error": "Something went wrong"}
    return render(request, 'users/login.html', context)


def registrationHandler(request):
    form = ""
    error = ''
    if request.method == 'GET':
        form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = form.errors

    context = {'form': form, 'error': error}

    return render(request, 'users/registration.html', context)
