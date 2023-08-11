from rest_framework.routers import DefaultRouter
from departments.api.views import DepartmentApiView

router_department=DefaultRouter()
router_department.register(
    prefix="department",
    basename="department",
    viewset=DepartmentApiView
)