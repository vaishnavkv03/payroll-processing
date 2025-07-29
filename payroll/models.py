# payroll/models.py

from django.db import models
from decimal import Decimal

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    
    def __str__(self):
        return self.name

class SalaryStructure(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2, help_text="House Rent Allowance")
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    
    def get_gross_salary(self):
        return self.basic_salary + self.hra + self.special_allowance

    def __str__(self):
        return f"Salary for {self.employee.name}"