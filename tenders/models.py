from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class tenders(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) 
    company = models.ForeignKey(User, on_delete=models.CASCADE)       


    def __str__(self):
        return self.title
  