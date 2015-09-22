from django.db import models

# Create your models here.


class Flot(models.Model):
    
    score = models.IntegerField()
    
    utc = models.IntegerField()