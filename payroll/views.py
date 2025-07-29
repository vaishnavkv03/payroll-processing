# payroll/views.py

from django.shortcuts import render, get_object_or_404
from .models import Employee
from .logic import calculate_payslip
import calendar

def generate_payslip_view(request, employee_id, month, year):
    employee = get_object_or_404(Employee, pk=employee_id)
    
    # For this example, we are hardcoding 2 days of Leave Without Pay (LWP).
    # In a real app, this would come from a user input form or another database model.
    lwp_days = 2
    
    # Get the total number of days in the requested month and year
    total_days_in_month = calendar.monthrange(year, month)[1]

    # Call the logic function to get all calculated salary data
    payslip_data = calculate_payslip(employee, lwp_days, total_days_in_month)
    
    # Prepare the context dictionary to pass data to the template
    context = {
        'payslip': payslip_data,
        'employee': employee,
        'month_year': f"{calendar.month_name[month]} {year}",
        'lwp_days': lwp_days,
        'total_days': total_days_in_month
    }
    
    return render(request, 'payroll/payslip_template.html', context)