from django.contrib import admin
from .models import Profile, Course, SessionID, Question

# Register your models here.
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(SessionID)
admin.site.register(Question)
