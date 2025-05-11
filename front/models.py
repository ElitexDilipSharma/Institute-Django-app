from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)    
    course_fees = models.CharField(max_length=100)    
    student_email = models.CharField(max_length=100)    
    
class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)    
    