from rest_framework.serializers import ModelSerializer
from vigilant.models import Vigilant

class VigilantSerializer(ModelSerializer):
    class Meta:
        model=Vigilant
        fields="__all__"