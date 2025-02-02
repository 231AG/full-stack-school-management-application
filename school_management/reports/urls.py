from django.urls import path
from .views import (
    AttendanceReportView,
    AcademicReportView,
    FinancialReportView,
)

urlpatterns = [
    # Attendance Reports
    path('attendance-reports/', AttendanceReportView.as_view(), name='attendance-reports'),

    # Academic Reports
    path('academic-reports/', AcademicReportView.as_view(), name='academic-reports'),

    # Financial Reports (if finance app is used)
    path('financial-reports/', FinancialReportView.as_view(), name='financial-reports'),
]