# school_app/serializers.py
from rest_framework import serializers
from .models import Instructor, Course, CurriculumUnit

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'instructor']

class CurriculumUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumUnit
        fields = ['id', 'name', 'course', 'description']
