from django.contrib import admin
from django.contrib import admin
from .models import Instructor, Course, CurriculumUnit

# Register your models here.

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(CurriculumUnit)
