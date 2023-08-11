from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from visit.models import Visit
from visit.api.serializer import VisitSerializer
from departments.models import Department
from datetime import datetime
import random

class VisitApiView(ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=VisitSerializer
    queryset=Visit.objects.all()
    
    def create(self, request, *args, **kwargs):
        try:
            if Department.objects.get(num_department=request.data["department"]).exists():
                department=Department.objects.get(num_department=request.data["department"])
                visit=Visit(
                    is_active=True,
                    token=random.randint(6, 999999),
                    department=department,
                )
                visit.save()
                return Response({"success":visit.token}, status=status.HTTP_201_CREATED)
            else:
                return Response(
                {"fail":"no se pudo crear el codigo de visita"},
                status=status.HTTP_404_NOT_FOUND
            )
        except:
            return Response(
                {"fail":"no se pudo crear el codigo de visita"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
    
    @action(
        detail=False,
        methods=["get"],
        url_path=r'department/(?P<num_department>\w+)',
    )
    def getVisitByDepartment(self,request,num_department=None):
        visits=Visit.objects.filter(department=num_department)
        token=random.randint(6, 999999)
        active_visit=[]
        for visit in visits:
            if(visit.is_active==True):
                active_visit.append(visit)
        serializer = VisitSerializer(active_visit, many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    @action(
        detail=False,
        methods=["patch"],
        url_path=r'validate'
    )
    def validateToken(self,request):
        token=request.data["token"]
        if Visit.objects.filter(token=token).exists():
            Visit.objects.filter(token=token).update(
                token='', is_active=False, entry_date=datetime.now()
            )
            return Response(
                {"sucsses":"Puede pasar"},
                status=status.HTTP_202_ACCEPTED
            )
        else:
            return Response(
                {"fail":"El token no es valido"},
                status=status.HTTP_401_UNAUTHORIZED
            )