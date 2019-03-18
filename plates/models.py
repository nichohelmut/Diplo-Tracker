from django.db import models


class Plate(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        plateNumber = models.IntegerField()
        street = models.CharField(max_length=255)
        zipCode = models.IntegerField()
        city = models.TextField(max_length=100)
        counter = models.IntegerField()
