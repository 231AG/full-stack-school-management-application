from django.urls import path
from .views import (
    ClassListView,
    ClassDetailView,
    SubjectListView,
    SubjectDetailView,
    StudentListView,
    StudentDetailView,
    TeacherListView,
    TeacherDetailView,
)

urlpatterns = [
    # Classes
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),

    # Subjects
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),

    # Students
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    # Teachers
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
]