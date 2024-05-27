from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry


# Register your models here.

from .models import *

admin.site.register(CoreUserProfile)
admin.site.register(LearningInstitution)
admin.site.register(Interest)


