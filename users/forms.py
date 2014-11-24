from django import forms

class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())
    re_password = forms.CharField(widget=forms.widgets.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.widgets.PasswordInput())
    