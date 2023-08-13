from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from departments.api.serializer import DepartmentSerializer
from departments.models import Department

class DepartmentApiView(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()
    
    @action(
        detail=False,
        methods=["get"],
        url_path=r'tenant/(?P<tenantId>\w+)'
    )
    def getDepartmentByUser(self,request,tenantId=None):
        departments=Department.objects.get(tenant=tenantId)
        serializer=DepartmentSerializer(departments)
        return Response(serializer.data, status=status.HTTP_200_OK)
    