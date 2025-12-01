from django.db import models

class student(models.Model):
    std_name = models.CharField(max_length=50)
    std_pin = models.IntegerField()
    
    
    
