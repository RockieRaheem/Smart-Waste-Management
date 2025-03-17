from django.db import models
from users.models import CustomUser

# Create your models here.
class GarbageRequest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class IllegalDumpingReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.TextField()
    image = models.ImageField(upload_to='dumping_reports/')
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending')
    reported_at = models.DateTimeField(auto_now_add=True)
