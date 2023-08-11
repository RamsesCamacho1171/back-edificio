from rest_framework.serializers import ModelSerializer
from departments.models import Department
from users.api.serializer import UserSerilizer

class DepartmentSerializer(ModelSerializer):
    tenant=UserSerilizer(read_only=True)
    class Meta:
        model=Department
        fields="__all__"

    