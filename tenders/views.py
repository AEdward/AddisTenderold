from django.shortcuts import render
from django.http import HttpResponse
from .models import tenders
import datetime
from django.views.generic import ListView, DetailView



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

def tender(request):
    
     context = {
         'posts': posts.objects.all()
     }
     return render (request,'tenders/tenders.html', context,{'title': 'Tenders'})      
     

class PostListView(ListView):
    model = tenders
    template_name = 'tenders/tenders.html'
    context_object_name = 'posts'
    ordering = ['date_posted']


class PostDetailView(DetailView):
    model = tenders


