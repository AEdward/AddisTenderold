from django import forms

from .models import Email_Sub
from . import views


class SubForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs = {'class' : 'form-control'}))
    class Meta:
        model = Email_Sub
        fields = ('full_name', 'email')
        widgets = {
            'full_name' : forms.TextInput(attrs = {'class' : 'form-control'}),         
            
               
        }