from django.db import models
import uuid
import datetime 

class Employees(models.Model):
    employee_id = models.CharField(max_length=40,default=uuid.uuid4(),null=False,unique=True)
    name =  models.CharField(max_length=60,null=False)
    Role = models.CharField(max_length=20,null=False)
    salary = models.CharField(max_length=16,null=False)
    date_hired = models.DateField(default=datetime.date.today)

    def __str__(self):
    	return self.name

