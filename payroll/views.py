# payroll/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from .logic import calculate_payslip
# Import the new form
from .forms import PayslipForm
import calendar

# Keep home_view and dashboard_view as they are...
def home_view(request):
    return render(request, 'payroll/home.html')

@login_required
def dashboard_view(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'payroll/dashboard.html', context)

# --- Add the new view for processing payslips ---
@login_required
def process_payslip_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    
    if request.method == 'POST':
        # If the form is submitted
        form = PayslipForm(request.POST)
        if form.is_valid():
            # Process the form data
            lwp_days = form.cleaned_data['lwp_days']
            month = int(form.cleaned_data['month'])
            year = int(form.cleaned_data['year'])
            
            total_days_in_month = calendar.monthrange(year, month)[1]
            payslip_data = calculate_payslip(employee, lwp_days, total_days_in_month)
            
            context = {
                'payslip': payslip_data,
                'employee': employee,
                'month_year': f"{calendar.month_name[month]} {year}",
            }
            # Render the FINAL payslip template
            return render(request, 'payroll/payslip_template.html', context)
    else:
        # If it's a GET request, show the empty form
        form = PayslipForm()

    context = {
        'form': form,
        'employee': employee
    }
    return render(request, 'payroll/process_payslip.html', context)
# --- End of new view ---

# We can now remove the old generate_payslip_view, as its logic is handled by the new view.