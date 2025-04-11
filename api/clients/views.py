from rest_framework import viewsets
from core.clients.models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer