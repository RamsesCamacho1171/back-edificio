from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from tenant.models import Tenant
from tenant.api.serializer import TenantSerializer

class TenantApiView(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=TenantSerializer
    queryset=Tenant.objects.all()
    
    @action(
        detail=False,
        methods=["get"],
        url_path=r'user/(?P<userId>\w+)'
    )
    def getTenantByuser(self,request, userId=None):
        tenant=Tenant.objects.get(info_user=userId)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data, status=status.HTTP_200_OK)