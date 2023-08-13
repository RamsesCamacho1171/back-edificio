from rest_framework.serializers import ModelSerializer
from departments.models import Department
from tenant.api.serializer import TenantSerializer

class DepartmentSerializer(ModelSerializer):
    tenant=TenantSerializer(read_only=True)
    class Meta:
        model=Department
        fields="__all__"

    