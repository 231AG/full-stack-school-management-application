from django.urls import path
from .views import (
    TimetableListView,
    TimetableDetailView,
    EventListView,
    EventDetailView,
)

urlpatterns = [
    # Timetables
    path('timetables/', TimetableListView.as_view(), name='timetable-list'),
    path('timetables/<int:pk>/', TimetableDetailView.as_view(), name='timetable-detail'),

    # Events
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]