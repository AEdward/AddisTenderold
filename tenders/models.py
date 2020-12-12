from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from notifications.models import Notification
from django.db.models.signals import post_save
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class tenders(models.Model):
    title = models.CharField(max_length = 200)
    body = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now) 
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 200, default = 'tech', null=True, blank=True)
    open_date = models.DateField() 
    close_date = models.DateField() 
    document = models.FileField(upload_to='media', default = 'todo.txt' )
  

    
    

    def user_post(sender, instance, *args, **kwargs):
        ten = instance
        title = ten.title
        text_preview = ten.body[:90]
        sender = ten.company
        notify = Notification(title=title, sender=sender, text_preview=text_preview ,notification_type=1)
        notify.save()


   

#Post
post_save.connect(tenders.user_post, sender=tenders)





