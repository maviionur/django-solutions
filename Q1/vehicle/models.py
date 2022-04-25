from pyexpat import model
from django.db import models
from vehicle.model_managers import NavigationRecordManager

# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):

        return self.plate

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=False, blank=False)
    latitude = models.FloatField(null=False, blank=False)
    longitude = models.FloatField(null=False, blank=False)

    objects = NavigationRecordManager()

    def __str__(self):

        return f"{self.datetime.strftime('%Y/%m/%d, %H:%M:%S')} - {self.vehicle.plate}"