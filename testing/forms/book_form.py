import re
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
    def clean_name(self): 
        name = self.cleaned_data.get('name')
        if re.findall(r"[^\w ]", name):
            raise forms.ValidationError(("Invalid book name"), code="invalid")
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        publish_date = cleaned_data.get('publish_date')
        if publish_date and publish_date.year < 1200:
            raise forms.ValidationError(("Books published earlier than 1200 AD are not supported"), code="invalid")
        return cleaned_data