from .models import tenders
from django import forms

'''
class postForm(forms.ModelForm):
    class Meta:
        model = tenders
        exclude = ('date_posted',)
        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'body' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'company' : forms.Select(attrs = {'class' : 'form-control'}),
             'category' : forms.TextInput(attrs = {'class' : 'form-control'})
            
               
    }

'''
'''
class AddPost(forms.ModelForm):
    class Meta:
        model = tenders
        exclude = ['date_posted' ]
        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'body' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'company' : forms.Select(attrs = {'class' : 'form-control'}),
             'category' : forms.TextInput(attrs = {'class' : 'form-control'})
            
               
        }


'''