from rest_framework import serializers
from .models import Assignment, Exam, Grade, ProgressReport

# Assignment
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'subject', 'due_date', 'created_by']

# Exam
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'subject', 'date', 'total_marks']

# Grade
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'student', 'assignment', 'exam', 'score', 'remarks']

# Progress Report
class ProgressReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressReport
        fields = ['id', 'student', 'term', 'overall_grade', 'remarks']