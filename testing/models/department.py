from django.db import models

class Department(models.Model):
    def __init__(self) -> None:
        self.name = models.CharField(max_length=50)

    def __str__(self): 
        return f"DP {self.name}"