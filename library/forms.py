from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
