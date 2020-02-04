from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from argh import Catagory

# Create your models here.

class tenders(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length = 200, default = 'tech')


    def __str__(self):
        return self.title
    
    '''def get_absolute_url(self):
        return reverse ('detail', kwargs = {'pk': self.pk})
  '''