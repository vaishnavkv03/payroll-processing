# payroll/admin.py

from django.contrib import admin
from .models import Employee, SalaryStructure

admin.site.register(Employee)
admin.site.register(SalaryStructure)