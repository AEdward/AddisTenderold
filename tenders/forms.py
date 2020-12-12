from .models import tenders, Catagory
from django import forms
#from ckeditor.fields import RichTextField

choices = Catagory.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class TendersForm(forms.ModelForm):
    class Meta:
        model = tenders
        fields = ('title', 'category', 'company','body', 'open_date','close_date','document')



        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'open_date':forms.DateTimeInput(attrs={'class': 'form-control','data-target': 'datetimepicker'}),
            'close_date':forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
            
        }


#class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    #file = forms.FileField()


    