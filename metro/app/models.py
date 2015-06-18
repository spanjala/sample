from django.db import models

# Create your models here.


class Metro(models.Model):
    
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

