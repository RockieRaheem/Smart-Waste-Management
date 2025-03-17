from django.db import models
from users.models import CustomUser

class WasteRequest(models.Model):
    REQUEST_TYPES = [
        ('collection', 'Waste Collection Request'),
        ('illegal_dumping', 'Illegal Dumping Report'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending Assignment'),
        ('assigned', 'Assigned'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    ]
    resident = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="waste_requests")
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    image = models.ImageField(upload_to="waste_images/", blank=True, null=True)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    assigned_driver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tasks")
    assigned_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_requests")
    rejected_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="rejected_tasks")  # New field
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def company_dashboard_status(self):
        if self.status == "assigned" and self.assigned_driver:
            return f"Assigned to {self.assigned_driver.username}"
        elif self.status == "accepted" and self.assigned_driver:
            return f"Accepted by {self.assigned_driver.username}"
        elif self.status == "rejected" and self.rejected_by:
            return f"Rejected by {self.rejected_by.username}"
        elif self.status == "completed" and self.assigned_driver:
            return f"Completed by {self.assigned_driver.username}"
        elif self.status == "pending":
            return "Pending Assignment"
        return "Unknown"

    def driver_dashboard_status(self):
        if self.status in ["accepted", "rejected", "completed"]:
            return self.status.capitalize()
        elif self.status == "assigned":
            return "Assigned"
        return "Pending Assignment"

    def __str__(self):
        return f"{self.request_type} by {self.resident.username} at {self.location} - {self.company_dashboard_status()}"