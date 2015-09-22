from django.db import models
# Create your models here.



class Redditor(models.Model):
    
    username = models.CharField(max_length=20)
    birthday_utc = models.IntegerField(default=0)
    
    

class SampleChart(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    
    
