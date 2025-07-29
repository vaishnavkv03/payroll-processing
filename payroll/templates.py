<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Payslip for {{ payslip.employee_name }}</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; margin: 40px; color: #333; }
        .payslip-box { border: 1px solid #ccc; padding: 25px; max-width: 600px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.05); border-radius: 8px; }
        .header { text-align: center; margin-bottom: 25px; border-bottom: 2px solid #f0f0f0; padding-bottom: 15px; }
        h2, h4 { color: #111; }
        .row { display: flex; justify-content: space-between; padding: 8px 5px; border-bottom: 1px solid #eee; }
        .row span:first-child { color: #555; }
        .row span:last-child { font-weight: bold; }
        .total { font-size: 1.1em; font-weight: bold; background-color: #f7f7f7; }
        .net-salary { font-size: 1.25em; font-weight: bold; background-color: #e8f5e9; color: #2e7d32; margin-top: 15px; padding: 12px 5px; text-align: center; border-radius: 5px; }
    </style>
</head>
<body>

    <div class="payslip-box">
        <div class="header">
            <h2>Payslip</h2>
            <p>For the period: <b>{{ month_year }}</b></p>
            <p>Employee: <b>{{ employee.name }}</b> (ID: {{ employee.employee_id }})</p>
        </div>

        <h4>Earnings</h4>
        <div class="row"><span>Monthly Gross Salary</span> <span>₹ {{ payslip.monthly_gross }}</span></div>
        <div class="row"><span>LWP Deduction (for {{ lwp_days }} days)</span> <span>- ₹ {{ payslip.lwp_deduction }}</span></div>
        <div class="row total"><span>Earned Gross Salary</span> <span>₹ {{ payslip.earned_gross }}</span></div>

        <br>

        <h4>Deductions</h4>
        <div class="row"><span>Provident Fund (PF)</span> <span>₹ {{ payslip.employee_pf }}</span></div>
        <div class="row"><span>Professional Tax (PT)</span> <span>₹ {{ payslip.professional_tax }}</span></div>
        <div class="row"><span>TDS (Income Tax)</span> <span>₹ {{ payslip.tds }}</span></div>
        <div class="row total"><span>Total Deductions</span> <span>₹ {{ payslip.total_deductions }}</span></div>

        <div class="net-salary">
            <span>Net Salary Payable: ₹ {{ payslip.net_salary }}</span>
        </div>
    </div>

</body>
</html>