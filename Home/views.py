from django.shortcuts import render
from django.http import HttpResponse
import datetime
from tenders import views

def home(request):
    return render (request,'Home/index.html',{'title':'Home'})

def index(request):
        
    context = {
         'posts':tenders.objects.all()
    }

    return render (request,'tenders/tenders.html', context,{'title':'tenders'})      

posts = [

    {
        'company' : 'Anahom',
        'title' : 'Tender Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'company' : 'Tsegawu',
        'title' : 'Tender Post 2',
        'content': 'secnod post content',
        'date_posted': 'August 28, 2019',
    }
]