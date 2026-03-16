from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=200,blank=True)
    origin_icao = models.CharField(max_length=4, blank=True)
    dest = models.CharField(max_length=200)
    dest_icao = models.CharField(max_length=4, blank=True)
    completed = models.BooleanField(blank=True, default=False)

# Create your models here.
