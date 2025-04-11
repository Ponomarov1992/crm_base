from django.db import models
from core.clients.models import Client

class Consultation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='consultations')
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='new')  # new, canceled, completed

    def __str__(self):
        return f"Consultation #{self.id} - {self.client.name}"