from rest_framework import serializers
from core.consultations.models import Consultation

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'