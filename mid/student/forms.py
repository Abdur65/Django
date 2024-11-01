from django import forms
from student.models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'grade', 'subject']
