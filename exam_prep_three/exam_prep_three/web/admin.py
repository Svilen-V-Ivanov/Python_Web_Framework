from django.contrib import admin

from exam_prep_three.web.models import Profile, Book


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass
