from rest_framework import generics, permissions
from .models import FeeCollection, Salary
from .serializers import FeeCollectionSerializer, SalarySerializer

# Fee Collection List and Detail
class FeeCollectionListView(generics.ListCreateAPIView):
    queryset = FeeCollection.objects.all()
    serializer_class = FeeCollectionSerializer
    permission_classes = [permissions.IsAdminUser]

class FeeCollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeeCollection.objects.all()
    serializer_class = FeeCollectionSerializer
    permission_classes = [permissions.IsAdminUser]

# Salary List and Detail
class SalaryListView(generics.ListCreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [permissions.IsAdminUser]

class SalaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [permissions.IsAdminUser]