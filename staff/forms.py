from django import forms
from .models import Staff, Position

class addStaff(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'surname', 'last_name', 'position', 'date_except']



class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'surname', 'last_name', 'position', 'date_except']


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title']