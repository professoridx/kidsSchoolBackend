from django.db import models
from Subjects.models import Subjects_Details

# Create your models here.
class Students(models.Model):
    choice_gen=[
        ('Male','Male'),
        ('Female','Female')
    ]

    #student Data Model
    stduent_name=models.CharField(max_length=25,blank=False)
    stduent_id = models.CharField(max_length=11, blank=False)
    student_father = models.CharField(max_length=25, blank=False)
    student_mother = models.CharField(max_length=25, blank=False)
    student_Gender=models.CharField(max_length=23,blank=True,null=True,choices=choice_gen)
    student_birthdate=models.DateField(auto_now_add=False)
    student_photo=models.ImageField(blank=True)
    stduent_Address=models.TextField(blank=False)


class StudentSub(models.Model):
    studetsub=models.ForeignKey(Subjects_Details, on_delete=models.CASCADE)
    subject_marks=models.DecimalField()
    subject_grade=models.CharField(max_length=5)



class Exam(models.Model):
    examdate=models.DateField(blank=True)
    examSyleBus=models.TextField(blank=True)
    
    