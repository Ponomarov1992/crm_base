from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from api.clients.views import ClientViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='TID CRM API',
        default_version='v1',
        description='Test description',
        contact=openapi.Contact(email='ponomarovcompany@gmail.com'),
    ),
    public=True,
)

router = routers.SimpleRouter()
router.register(r'clients', ClientViewSet, basename='clients')

urlpatterns = router.urls
urlpatterns.extend(
    [
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
)
