from rest_framework.routers import DefaultRouter
from visit.api.views import VisitApiView

router_visit=DefaultRouter()
router_visit.register(
    prefix='visit',
    basename='visit',
    viewset=VisitApiView
)