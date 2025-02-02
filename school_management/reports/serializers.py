from rest_framework import serializers

# Attendance Report
class AttendanceReportSerializer(serializers.Serializer):
    student = serializers.CharField()
    total_present = serializers.IntegerField()
    total_absent = serializers.IntegerField()

# Academic Report
class AcademicReportSerializer(serializers.Serializer):
    student = serializers.CharField()
    average_score = serializers.DecimalField(max_digits=5, decimal_places=2)
    overall_grade = serializers.CharField()

# Financial Report (if finance app is used)
class FinancialReportSerializer(serializers.Serializer):
    total_fees_collected = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_salaries_paid = serializers.DecimalField(max_digits=10, decimal_places=2)