from rest_framework import mixins, viewsets

from api.clients.filters import ClientFilter
from core.clients.models import Client
from core.utils.permissions import BotAPIPermission

from .serializers import ClientInfoSerializer, CreateClientSerializer


class ClientViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    authentication_classes = []
    permission_classes = (BotAPIPermission,)
    queryset = Client.objects.filter(is_active=True)
    SERIALIZERS = {'create': CreateClientSerializer, 'retrieve': ClientInfoSerializer, 'list': ClientInfoSerializer}
    filterset_class = ClientFilter

    def get_serializer_class(self):
        return self.SERIALIZERS.get(self.action)
