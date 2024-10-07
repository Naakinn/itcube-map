from django.db import models
from .employee import Employee 

class Profile(models.Model): 
    def __init__(self) -> None:
        self.employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
        self.bio = models.TextField(); 
        self.location = models.CharField(max_length=100)

    def __str__(self):
            return f"PF {self.employee}"
            