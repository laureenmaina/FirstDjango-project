from django import forms
from MYAPP.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstname','lastname','Age','phone_number']


class EmployeeForm(forms.Form):
        firstname=forms.CharField(label="Enter firstname",max_length=50)
        lastname=forms.CharField(label="Enter lastname",max_length=50)
        Age=forms.IntegerField(label="Enter age")
        phonenumber=forms.IntegerField(label="Enter phonenumber")

