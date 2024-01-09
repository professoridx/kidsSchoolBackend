from rest_framework import serializers
from .models import Teacher_Credit

class Teacher_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Teacher_Credit
        fields='__all__'
        
        