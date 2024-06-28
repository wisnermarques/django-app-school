# school_app/forms.py
from django import forms
from .models import Instructor, Course, CurriculumUnit

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'instructor']

class CurriculumUnitForm(forms.ModelForm):
    class Meta:
        model = CurriculumUnit
        fields = ['name', 'course', 'description']
