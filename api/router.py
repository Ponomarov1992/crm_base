from rest_framework.routers import DefaultRouter
from api.clients.views import ClientViewSet
from api.consultations.views import ConsultationViewSet
from api.users.views import UserViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'users', UserViewSet)