from django.shortcuts import render
from django.http import HttpResponse
import datetime

def contact(request):
    return render (request,'contact/contact.html',{'title':'contact'})

