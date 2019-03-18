from django.db import models


class Plate(models.Model):
        plateNumber = models.IntegerField()
        street = models.CharField(max_length=255)
        zipCode = models.IntegerField()
        city = models.TextField(max_length=100)
