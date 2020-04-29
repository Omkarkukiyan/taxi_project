from django import forms 
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class DriverRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email=forms.EmailField()
    license_id = forms.CharField(max_length=10, validators=[alphanumeric])
    profile_pic = forms.ImageField(required=False) 
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','license_id','password1','password2','profile_pic']