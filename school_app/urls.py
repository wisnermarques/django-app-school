# school_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstructorViewSet, CourseViewSet, CurriculumUnitViewSet

router = DefaultRouter()
router.register(r'instructors', InstructorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'curriculum-units', CurriculumUnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
