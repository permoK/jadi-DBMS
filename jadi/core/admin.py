from django.contrib import admin


# Register your models here.

from .models import *


admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Lecturer)
admin.site.register(ResourceCategory)
admin.site.register(AcademicResource)
admin.site.register(AuthorizedUploader)

