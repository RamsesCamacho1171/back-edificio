from rest_framework.routers import DefaultRouter
from tenant.api.views import TenantApiView

router_tenant=DefaultRouter()
router_tenant.register(
    prefix='tenant',
    basename='tenant',
    viewset=TenantApiView
)