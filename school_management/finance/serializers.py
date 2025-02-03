from rest_framework import serializers
from .models import FeeCollection, Salary

# Fee Collection
class FeeCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeCollection
        fields = ['id', 'student', 'amount', 'date_paid', 'payment_method']

# Salary
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['id', 'teacher', 'amount', 'date_paid', 'payment_method']