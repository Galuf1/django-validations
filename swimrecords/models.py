from django.db import models
from .validator import *

class SwimRecord(models.Model):
    # pass # delete me when you start writing in validations
    first_name = models.CharField(max_length=50,blank=False,null=False)
    last_name = models.CharField(max_length=50,blank=False,null=False)
    team_name = models.CharField(max_length=50,blank=False,null=False)
    relay = models.BooleanField(null=False,blank=False,default=True)
    stroke = models.CharField(max_length=50,validators=[validate_stroke])
    distance = models.IntegerField(validators=[min_distance])
    record_date = models.DateTimeField(validators=[validate_date])
    record_broken_date = models.DateTimeField(validators=[validate_record_date])
