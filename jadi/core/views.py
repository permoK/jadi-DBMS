from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

#Create your views here.


def index(request):
    return render(request, 'index.html')


class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class LearningInstitutionView(viewsets.ModelViewSet):
    queryset = LearningInstitution.objects.all()
    serializer_class = LearningInstitutionSerializer


class InterestView(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

# Compare this snippet from urls.py:
