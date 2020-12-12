from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views.generic import (ListView)
from .forms import SubForm
from . import models
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
def home(request):    
     return render (request,'Home/index.html')
   
    
    
  
def email(request):

    
    template = "Home/index.html"


    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubForm()
    context = {
        'form':form,
    }
    return render (request, template,context)


'''

def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt
def email(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content ='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': SubForm()})
    else:
        return render(request, 'index.html', {'form': SubForm()})
'''