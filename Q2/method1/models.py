from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):

        return f'{self.latitude} - {self.longitude}'

class Operation(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):

        return f'{self.name}'


class BinOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()