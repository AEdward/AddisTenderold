from .models import tenders
from django import forms

'''
class postForm(forms.ModelForm):
    class Meta:
        model = tenders
        exclude = ('date_posted',)
'''
'''

class AddPost(forms.ModelForm):
    class Meta:
        model = tenders
        exclude = ['date_posted' ]
        widgets = {
            'title' : forms.TextInput(attrs = {'class' : 'form-control', 'id' : 'con'}),
            'body' : forms.Textarea(attrs = {'class' : 'form-control', 'id' : 'con'}),
            'company' : forms.Select(attrs = {'class' : 'form-control', 'id' : 'con'})
            
               
        }


'''