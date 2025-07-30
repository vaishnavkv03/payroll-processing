# payroll/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # Add the path for our new processing page
    # This captures the employee's ID from the URL
    path('employee/<int:employee_id>/', views.process_payslip_view, name='employee_detail'),
]