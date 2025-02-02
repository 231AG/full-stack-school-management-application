from django.urls import path
from .views import (
    AssignmentListView,
    AssignmentDetailView,
    ExamListView,
    ExamDetailView,
    GradeListView,
    GradeDetailView,
    ProgressReportListView,
    ProgressReportDetailView,
)

urlpatterns = [
    # Assignments
    path('assignments/', AssignmentListView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),

    # Exams
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),

    # Grades
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grades/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),

    # Progress Reports
    path('progress-reports/', ProgressReportListView.as_view(), name='progress-report-list'),
    path('progress-reports/<int:pk>/', ProgressReportDetailView.as_view(), name='progress-report-detail'),
]