from django.contrib import admin


# Register your models here.

from .models import *


admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Lecturer)
admin.site.register(Note)
# admin.site.register(savedNote)
# admin.site.register(Comment)

