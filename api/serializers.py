from rest_framework import serializers
from api.models import Employees


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        