from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def about(request):
    
    return render (request,'About/about.html')