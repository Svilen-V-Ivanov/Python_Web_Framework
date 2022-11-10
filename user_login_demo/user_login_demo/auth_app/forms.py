# auth_app/views
from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from user_login_demo.auth_app.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        # fields = ('first_name', 'last_name', 'username')
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', )
        field_classes = {"username": auth_forms.UsernameField}


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')

    # Save with data for profile
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
        )
        if commit:
            profile.save()

        return user

        # Save with empty profile
        # def save(self, commit=True):
        #     user = super().save(commit=commit)
        #     profile = Profile(
        #         user=user,
        #     )
        #     if commit:
        #         profile.save()

    # For demo purposes
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     user.username = user.first_name + '-' + user.last_name
    #     if commit:
    #         user.save()
    #     return user