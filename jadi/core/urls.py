from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# from . import views

# router = DefaultRouter()
# router.register('user-profile', UserProfileView)
# router.register('learning-institutions', LearningInstitutionView)
# router.register('interests', InterestView)
router = DefaultRouter()
router.register(r'user-profiles', UserProfileView, basename='userprofile')
router.register(r'learning-institutions', LearningInstitutionView, basename='learninginstitution')
router.register(r'interests', InterestView, basename='interest')

urlpatterns = [
    path('', index),
    path('api/v1/user/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
