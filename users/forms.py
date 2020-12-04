from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs = {'class' : 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-control'}))


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control'}) ,
         
        
            
               
        }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class' : 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control'}),         
            
               
        }
        

class ProfileUpdateForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ['image']
       
