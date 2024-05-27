from django.contrib import admin


# Register your models here.

from .models import *

admin.site.register(CoreUserProfile)
admin.site.register(LearningInstitution)
admin.site.register(Interest)
