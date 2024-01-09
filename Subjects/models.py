from django.db import models
from Teacher.models import Teacher_Credit


# Create your models here.
class Subjects_Details(models.Model):
    subject_name=models.CharField(max_length=23,blank=True)
    subject_code=models.CharField(max_length=12)
    subject_catagory=models.CharField(max_length=12)
    subject_details=models.TextField(blank=False)
    subjects_marks=models.IntegerField(blank=True)
    subject_recommend_books=models.TextField(blank=True)
    subject_cedit=models.IntegerField(blank=True)
    subject_teacher=models.ForeignKey(Teacher_Credit, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.subject_name
    
    


    
    
    
