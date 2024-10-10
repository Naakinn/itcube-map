from django.db import models

# from django.contrib.auth.models import User
from .department import Department
from .project import Project 

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hire_date = models.DateField(null=True) 
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return f"EM {self.last_name} {self.first_name} <{self.email}>"
