from rest_framework import generics, permissions
from .serializers import AttendanceReportSerializer, AcademicReportSerializer, FinancialReportSerializer

# Attendance Reports
class AttendanceReportView(generics.ListAPIView):
    serializer_class = AttendanceReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Custom logic to generate attendance reports
        pass

# Academic Reports
class AcademicReportView(generics.ListAPIView):
    serializer_class = AcademicReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Custom logic to generate academic reports
        pass

# Financial Reports (if finance app is used)
class FinancialReportView(generics.ListAPIView):
    serializer_class = FinancialReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Custom logic to generate financial reports
        pass