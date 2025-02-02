from rest_framework import generics, permissions
from .models import Attendance
from .serializers import AttendanceSerializer, AttendanceReportSerializer

# Attendance List and Detail
class AttendanceListView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Mark Attendance
class AttendanceMarkView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

# Attendance Reports
class AttendanceReportView(generics.ListAPIView):
    serializer_class = AttendanceReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Custom logic to generate attendance reports
        return Attendance.objects.filter(student=self.request.user.student_profile)