from django.db import models

from .employee import Employee

class Profile(models.Model): 
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    location = models.CharField(max_length=50)

    def __str__(self) -> str:
         return f"PF {self.employee}"