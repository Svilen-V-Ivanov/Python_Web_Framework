from django import forms

from exam_prep_four.web.models import Profile, Note


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BaseNote(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url', )


class CreateNote(BaseNote):
    pass


class EditNote(BaseNote):
    pass


class DeleteNote(BaseNote):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            #field.widget.attrs['disabled'] = 'disabled'