from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from vigilant.api.serializer import VigilantSerializer
from vigilant.models import Vigilant

class VigilantApiView(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=VigilantSerializer
    queryset=Vigilant.objects.all()
    
    @action(
        detail=False,
        methods=["get"],
        url_path=r'user/(?P<userId>\w+)'
    )
    def getTenantByuser(self,request, userId=None):
        tenant=Vigilant.objects.get(info_user=userId)
        serializer = VigilantSerializer(tenant)
        return Response(serializer.data, status=status.HTTP_200_OK)