from rest_framework import serializers
from .models import Attendance

# Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status']

# Attendance Report
class AttendanceReportSerializer(serializers.Serializer):
    student = serializers.CharField()
    total_present = serializers.IntegerField()
    total_absent = serializers.IntegerField()