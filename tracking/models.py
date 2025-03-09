from django.db import models

class GarbageTruck(models.Model):
    driver_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    current_location = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
