from django.db import models
from .author import Author

class Book(models.Model): 
    name = models.CharField(max_length=100) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    publish_date = models.DateField()

    def __str__(self) -> str:
        return f"BK \"{self.name}\" {self.author}"
