from django.urls import path
from .views import (
    AttendanceListView,
    AttendanceDetailView,
    AttendanceMarkView,
    AttendanceReportView,
)

urlpatterns = [
    # Attendance Records
    path('attendance/', AttendanceListView.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),

    # Mark Attendance
    path('mark-attendance/', AttendanceMarkView.as_view(), name='mark-attendance'),

    # Attendance Reports
    path('attendance-reports/', AttendanceReportView.as_view(), name='attendance-reports'),
]