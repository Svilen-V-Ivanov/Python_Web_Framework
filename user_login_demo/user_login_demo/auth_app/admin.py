from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from user_login_demo.auth_app.forms import SignUpForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_display = ['email', 'date_joined', 'last_login']
    ordering = ('email',)
    list_filter = ()
    add_form = SignUpForm
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'age'),
            },
        ),
    )
