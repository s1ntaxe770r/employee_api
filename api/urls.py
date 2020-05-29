from rest_framework import routers
from .api import EmployeesViewset

router = routers.DefaultRouter()

router.register('api/v1/employees/',EmployeesViewset,'employees')

urlpatterns = router.urls


