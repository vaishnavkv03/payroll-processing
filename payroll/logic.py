# payroll/logic.py

from decimal import Decimal

# NOTE: Professional Tax and TDS are simplified to fixed values for this example.
# In a real-world app, these would involve complex, slab-based calculations.
PROFESSIONAL_TAX = Decimal('200.00')
TDS_AMOUNT = Decimal('1500.00')

def calculate_payslip(employee, lwp_days, total_days_in_month):
    """
    Calculates the payslip for a given employee and month.
    """
    salary_struct = employee.salarystructure
    
    # 1. Calculate Gross Salary
    monthly_gross_salary = salary_struct.get_gross_salary()
    
    # 2. Calculate Per-Day Salary and LWP Deduction
    per_day_salary = monthly_gross_salary / total_days_in_month
    lwp_deduction = per_day_salary * lwp_days
    
    # 3. Calculate Earned Gross Salary
    earned_gross_salary = monthly_gross_salary - lwp_deduction
    
    # 4. Calculate Deductions
    # Provident Fund (PF) is 12% of Basic Salary
    employee_pf = salary_struct.basic_salary * Decimal('0.12')
    
    total_deductions = employee_pf + PROFESSIONAL_TAX + TDS_AMOUNT
    
    # 5. Calculate Net Salary
    net_salary = earned_gross_salary - total_deductions
    
    # Return a dictionary with all calculated values for the template
    return {
        'employee_name': employee.name,
        'monthly_gross': monthly_gross_salary,
        'lwp_deduction': round(lwp_deduction, 2),
        'earned_gross': round(earned_gross_salary, 2),
        'employee_pf': round(employee_pf, 2),
        'professional_tax': PROFESSIONAL_TAX,
        'tds': TDS_AMOUNT,
        'total_deductions': round(total_deductions, 2),
        'net_salary': round(net_salary, 2),
    }