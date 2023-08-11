from rest_framework.serializers import ModelSerializer
from visit.models import Visit

class VisitSerializer(ModelSerializer):
    class Meta:
        model=Visit
        fields="__all__"