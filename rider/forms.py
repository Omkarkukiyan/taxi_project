from django import forms 
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm




class RiderRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email=forms.EmailField()
    profile_pic = forms.ImageField(required=False) 
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','password1','password2','profile_pic']