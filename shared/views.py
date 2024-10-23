from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from shared.forms import LoginForm, SignupForm


def user_login(request):
    if request.method == 'POST':
        if (form := LoginForm(request.)).is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):
                login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', dict(form=form))


def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        if (form := SignupForm(request.)).is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', dict(form=form))
