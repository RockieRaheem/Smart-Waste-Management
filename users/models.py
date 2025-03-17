from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('resident', 'Resident'),
        ('driver', 'Truck Driver'),
        ('company', 'Waste Management Company'),
        ('officer', 'Municipal Officer'),
    )
   
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='resident')

    def __str__(self):
        return f"{self.username} ({self.role})"

    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    # Specify a related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # change this to whatever you want for the reverse accessor
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # change this to whatever you want for the reverse accessor
        blank=True
    )
    

