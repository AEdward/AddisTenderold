from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import datetime
from .forms import ContactForm




def contact(request):
    template = "contact/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {
        'form':form,
    }
    return render (request, template,context)



'''
def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form', message, settings.EMAIL_HOST_USER, ['yididyafantahu@gmail.com'],fail_silently=False)
	
    return render (request,'contact/contact.html',{'title':'contact'})

'''