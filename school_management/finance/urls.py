from django.urls import path
from .views import (
    FeeCollectionListView,
    FeeCollectionDetailView,
    SalaryListView,
    SalaryDetailView,
)

urlpatterns = [
    # Fee Collection
    path('fee-collections/', FeeCollectionListView.as_view(), name='fee-collection-list'),
    path('fee-collections/<int:pk>/', FeeCollectionDetailView.as_view(), name='fee-collection-detail'),

    # Salary Management
    path('salaries/', SalaryListView.as_view(), name='salary-list'),
    path('salaries/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
]