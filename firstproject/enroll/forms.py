from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class Fistform(UserCreationForm):
    password2 = forms.CharField(label='Conform password (again)',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'email'}

class Secondform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
