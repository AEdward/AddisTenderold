from django.shortcuts import render
from django.http import HttpResponse
import datetime
#from AddisTender.tenders import views, models
from django.views.generic import (ListView)
from tenders.models import tenders,Catagory
#from tenders.views import  PostListView

from django.views.generic import (ListView)


def home(request):
    
    return render (request,'Home/index.html',{'title':'Home'})



'''def index(request):
        
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

'''