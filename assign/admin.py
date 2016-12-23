from django.contrib import admin
from .models import EmployeeInfo, Assignment, Delegation

# Register your models here.

admin.site.register(EmployeeInfo)
admin.site.register(Assignment)
admin.site.register(Delegation)
