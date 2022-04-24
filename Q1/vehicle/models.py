from pyexpat import model
from django.db import models

# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=15, null=False, blank=False)


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True,  null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)