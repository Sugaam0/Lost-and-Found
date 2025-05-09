from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# board/models.py
class FoundItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_found = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    contact_info = models.CharField(max_length=100, help_text="Phone number or email")
    image = models.ImageField(upload_to='lost_found_images/', null=True, blank=True)  # Image field
    def __str__(self):
        return f"[{self.status.upper()}] {self.title}"
