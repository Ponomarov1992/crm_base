from django.db.models import TextChoices

class ConsultationStatus(TextChoices):
    NEW = 'new', 'New'
    CANCELED = 'canceled', 'Canceled'
    COMPLETED = 'completed', 'Completed'