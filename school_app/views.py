# school_app/views.py
from rest_framework import viewsets
from .models import Instructor, Course, CurriculumUnit
from .serializers import InstructorSerializer, CourseSerializer, CurriculumUnitSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CurriculumUnitViewSet(viewsets.ModelViewSet):
    queryset = CurriculumUnit.objects.all()
    serializer_class = CurriculumUnitSerializer
