from rest_framework import serializers
from .models import Timetable, Event

# Timetable
class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'class_name', 'day_of_week', 'period', 'subject', 'teacher']

# Event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'start_time', 'end_time', 'organizer']