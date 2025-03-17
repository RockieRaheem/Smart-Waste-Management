from django.db import models
from users.models import CustomUser  # Import the User model

# Create your models here.
class CollectionRoute(models.Model):
    company = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'company'})
    route_name = models.CharField(max_length=255)
    assigned_truck = models.CharField(max_length=50)  # Truck license plate
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.route_name} - {self.company.username}"
