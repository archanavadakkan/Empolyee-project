from .models import EmployeeData
from django import forms


class ModeForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = ['emp_no', 'name', 'address', 'emp_start_date', 'emp_end_date', 'img', 'status']
