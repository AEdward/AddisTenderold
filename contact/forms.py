from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'message')
        widgets = {
           'full_name' : forms.TextInput(attrs = {'class' : 'form-control',}),
         #  'email' : forms.EmailField(widget=forms.EmailInput(attrs = {'class' : 'form-control',})),
           'message' : forms.Textarea(attrs = {'class' : 'form-control', })
            
             
        }