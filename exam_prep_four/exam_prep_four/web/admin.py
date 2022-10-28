from django.contrib import admin

from exam_prep_four.web.models import Profile, Note


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    pass
