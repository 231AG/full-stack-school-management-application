from django.urls import path
from .views import (
    NotificationListView,
    NotificationDetailView,
    AnnouncementListView,
    AnnouncementDetailView,
)

urlpatterns = [
    # Notifications
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),

    # Announcements
    path('announcements/', AnnouncementListView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>/', AnnouncementDetailView.as_view(), name='announcement-detail'),
]