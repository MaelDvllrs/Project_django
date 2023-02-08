from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='', widget=forms.TextInput(attrs={'id': 'box-key', 'placeholder': 'username'}))
    password = forms.CharField(max_length=63, label='', widget=forms.PasswordInput(attrs={'id': 'box-key', 'placeholder': 'password'}))