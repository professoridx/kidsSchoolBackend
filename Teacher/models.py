from django.db import models

# Create your models here.te
class Teacher_Credit(models.Model):
    teacher_name=models.CharField(max_length=30)
    teacher_deg=models.CharField(max_length=30)
    teacher_about=models.TextField(blank=True)
    teacher_photo=models.ImageField(blank=True)
    teacher_mail=models.TextField(max_length=39)
    teacher_id=models.CharField(max_length=20)
    teacher_resume=models.FileField(blank=True)
    
    def __str__(self):
        return self.teacher_name
    
