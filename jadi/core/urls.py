from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# from . import views

router = DefaultRouter()
router.register('user-profile', UserProfileView)
router.register('learning-institution', LearningInstitutionView)
router.register('interest', InterestView)


urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
