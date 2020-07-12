from django.db import models

# Create your models here.
class Forms(models.Model):
    Location = models.CharField(max_length=50)
    Incident_Desc = models.CharField(max_length=200)
    Incident_Loc = models.CharField(max_length=200)
    Date = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)
    Initial_Security = models.CharField(max_length=50)
    Suspected_Cause = models.CharField(max_length=100)
    Actions = models.CharField(max_length=200)
    Incident_Type = models.CharField(max_length=20)
    Reported_by = models.CharField(max_length=50)

