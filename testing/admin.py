from django.contrib import admin
from .models import Employee, Department, Profile, Project

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(Project)