from django.shortcuts import render
from django.http import HttpResponse
from .models import tenders
import datetime

def tenders(request):
     all_tenders = tenders.objects.order_by('-pubdate')
     context = {"all_tenders" : all_tenders}
     return render (request,'tenders/tenders.html',context)

