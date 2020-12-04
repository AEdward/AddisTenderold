from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class tenders(models.Model):
    title = models.CharField(max_length = 200)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 200, default = 'tech', null=True, blank=True)
    open_date = models.DateField(default=timezone.now) 
    close_date = models.DateField(default=timezone.now) 
  

    def __str__(self):
        return self.title




