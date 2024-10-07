from django.db import models
from django.contrib.auth.models import User
from .department import Department
from .project import Project

# GxtBW85vDYsSY8yT
class Employee(models.Model): 
    def __init__(self) -> None:
        self.first_name = models.CharField(max_length=50)
        self.last_name = models.CharField(max_length=50)
        self.email = models.EmailField(unique=True)
        self.department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
        self.projects = models.ManyToManyField(Project)
        self.user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

        def __str__(self):
            return f"EM {self.last_name} {self.first_name} <{self.email}>"