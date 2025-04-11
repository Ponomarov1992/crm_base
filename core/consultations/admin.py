from django.contrib import admin
from .models import Consultation

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "status", "created_at")
    search_fields = ("client__name",)