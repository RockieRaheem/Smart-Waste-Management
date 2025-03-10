from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('driver', 'Truck Driver'),
        ('officer', 'Municipal Officer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return f"{self.username} ({self.role})"



