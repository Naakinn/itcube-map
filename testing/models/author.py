from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"AU {self.first_name} {self.surname}"
