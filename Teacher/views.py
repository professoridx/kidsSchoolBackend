from django.shortcuts import render
from .serializer import Teacher_Serilizer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Teacher_Credit


class Teacher_api_viwes(ListCreateAPIView):
   
   dataset_teacher=Teacher_Credit.objects.all()
   
   teacher_seril=Teacher_Serilizer
   

class DataUpdate(RetrieveUpdateDestroyAPIView):
      dataset_teacher=Teacher_Credit.objects.all()
      teacher_seril=Teacher_Serilizer
      
   
