from django.shortcuts import render, redirect
from users import forms
from django.contrib import auth

def signup(request):
    errors = []
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_password']
            try:
                user = auth.models.User.objects.get(username=username)
                return redirect('accounts:login')
            except auth.models.User.DoesNotExist:
                if password != re_password:
                    errors.append('The passwords did not match, try again!')
                else:
                    auth.models.User.objects.create_user(username, email, password)
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    return redirect('beverages:hello')
    else:
        form = forms.SignupForm()
    return render(request, 'users/signup.html', {'form': form, 'errors': errors})

def login(request):
    errors = []
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('beverages:hello')
                else:
                    errors.append('The password is valid, but the account has been disabled!')
            else:
                errors.append('The username and password were incorrect')
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form, 'errors': errors})

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')
