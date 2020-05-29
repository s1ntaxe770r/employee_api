from django.db import models
import uuid 

class Employees(models.Model):
    employee_id = models.CharField(max_length=40,default=uuid.uuid4(),null=False,unique=True)
    name =  models.CharField(max_length=60,null=False)
    Role = models.CharField(max_length=20,null=False)
    salary = models.CharField(max_length=16,null=False)

    def __str__(self):
    	return self.employee_id

