from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView
from student.models import Student, Grade
from student.forms import StudentForm
from django.urls import reverse_lazy


class StudentListView(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"
    
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy("student_list")
    



