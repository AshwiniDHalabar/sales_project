from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.PasswordInput()
    confirmpassword = forms.CharField()
    phone_no = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password2','phone_no']