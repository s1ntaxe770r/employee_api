from rest_framework import routers
from django.urls import path,include
from .api import EmployeesViewset

router = routers.DefaultRouter()

router.register('employees',EmployeesViewset,'employees')

urlpatterns = [ path('api/v1/',include(router.urls))]


