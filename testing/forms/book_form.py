from django import forms
from ..models import Book

class BookForm(forms.ModelForm): 
    class Meta: 
        model = Book 
        fields = ["name", "author", "publish_date"]
        labels = { 
            "name": "Name", 
            "author": "Author",
            "publish_date": "Publish date"
        }
        widgets = { 
            "name": forms.TextInput(attrs={"class": "form-control", "maxlength": 20}), 
            "author": forms.Select(attrs={"class": "form-select"}), 
            "publish_date": forms.DateInput(attrs={"class": "form-control", "type": "date"})
        }