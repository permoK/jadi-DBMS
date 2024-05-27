from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class LearningInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningInstitution
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

# Compare this snippet from views.py:
