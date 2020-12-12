from django.db import models
from tenders.models import tenders,Catagory
from tenders.views import CategoryView

# Create your models here.
class Email_Sub(models.Model):
    full_name = models.CharField(max_length=50)   
    email = models.EmailField()    
   # message = models.TextField()

    def __str__(self):
        return f'{self.full_name}'