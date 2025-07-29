# payroll_system/urls.py

from django.contrib import admin
from django.urls import path
from payroll.views import generate_payslip_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL format: /payslip/employee_id/month/year/
    # Example: /payslip/1/7/2025/ for employee with ID 1, for July 2025
    path('payslip/<int:employee_id>/<int:month>/<int:year>/', generate_payslip_view, name='generate_payslip'),
]