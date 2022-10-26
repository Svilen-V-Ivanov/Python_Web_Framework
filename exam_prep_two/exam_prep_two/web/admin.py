from django.contrib import admin

from exam_prep_two.web.models import Profile, Game


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Game)
class AdminGame(admin.ModelAdmin):
    pass
