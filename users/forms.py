from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control1'}) ,
            'email' : forms.TextInput (attrs = {'class' : 'form-control1', 'type': 'email'}), 
            'password1' : forms.TextInput (attrs = {'class' : 'form-control1', 'type': 'password'}),
            'password2' : forms.TextInput (attrs = {'class' : 'form-control1', 'type': 'password'}),
        
            
               
        }
'''
        
        username = forms.CharField(
            widget = forms.TextInput (attrs = {'class' : 'form-control'})    
        )
            
        email = forms.EmailField(
            required = True, widget = forms.TextInput (attrs = {'class' : 'form-control'})    
        )
        password1 = forms.CharField(
            widget = forms.TextInput (attrs = {'class' : 'form-control', 'type': 'password'})    
        )
        password2 = forms.CharField(
           widget = forms.TextInput (attrs = {'class' : 'form-control' , 'type': 'password' })    
        )
            
               
        '''





class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username' : forms.TextInput(attrs = {'class' : 'form-control', 'id' : 'con'}),
            
            
               
        }
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
       
