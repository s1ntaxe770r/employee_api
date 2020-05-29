from api.models import Employees
from .serializers import  EmployeesSerializer
from rest_framework import viewsets 


class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class =  EmployeesSerializer


