from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime


class Slot(models.Model):
    startTime = models.DateTimeField(blank = False)
    endTime = models.DateTimeField(blank = False)
    
    
class UserDetails(models.Model):
    email = models.EmailField(max_length = 254, blank = False)
    username = models.CharField(max_length=200,blank = False)
    password = models.CharField(max_length=200,blank = False)
    userType = models.CharField(max_length=200,blank = False)
    scheduledInterviews = models.ManyToManyField( UserDetails )
    
    

class InterviewDetails(models.Model):
    participants = models.ManyToManyField( UserDetails )


