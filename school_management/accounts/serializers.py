from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# User Registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_superadmin', 'is_admin', 'is_teacher', 'is_parent', 'is_student']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_superadmin = validated_data.get('is_superadmin', False)
        user.is_admin = validated_data.get('is_admin', False)
        user.is_teacher = validated_data.get('is_teacher', False)
        user.is_parent = validated_data.get('is_parent', False)
        user.is_student = validated_data.get('is_student', False)
        user.save()
        return user

# User Login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# User Profile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'date_of_birth', 'profile_picture']

# User List and Detail
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superadmin', 'is_admin', 'is_teacher', 'is_parent', 'is_student', 'profile']