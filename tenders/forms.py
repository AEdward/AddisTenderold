from .models import tenders
from django import forms


class postform(forms.ModelForm):
    class Meta:
        model = tenders
        exclude = ('pubdate')