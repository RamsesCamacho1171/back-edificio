from rest_framework.routers import DefaultRouter
from vigilant.api.views import VigilantApiView

router_vigilant=DefaultRouter()
router_vigilant.register(
    prefix='vigilant',
    basename='vigilant',
    viewset=VigilantApiView
)