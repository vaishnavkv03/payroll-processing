# payroll/forms.py

from django import forms
import datetime

# Get the current year
current_year = datetime.date.today().year

# Define choices for month and year
MONTH_CHOICES = [
    (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
    (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
    (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')
]

YEAR_CHOICES = [(year, year) for year in range(current_year - 1, current_year + 2)]

class PayslipForm(forms.Form):
    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES, initial=current_year)
    lwp_days = forms.IntegerField(
        label="Days of Leave Without Pay (LWP)",
        min_value=0,
        initial=0,
        required=True
    )