from django.contrib import admin


# Register your models here.

from .models import UserProfile, Note #, Comment


admin.site.register(UserProfile)
admin.site.register(Note)
# admin.site.register(Comment)

