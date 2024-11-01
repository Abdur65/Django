from django.db import models

class Grade(models.Model): 
    subject = models.CharField(max_length=50)
    grade = models.CharField(max_length=5)
    
    def __str__(self):
        return self.grade

class Student(models.Model):
    student_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    grade = models.ManyToManyField(Grade)
    
    def __str__(self):
        return self.name
    
    
