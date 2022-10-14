from django import forms


class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )
    MAX_LENGTH = 30
    MAX_LENGTH_STORY = 200
    your_name = forms.CharField(
        max_length=MAX_LENGTH,
        label='Your name:',
        help_text='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            },
        )
    )

    age = forms.IntegerField(
        required=False,
        label='Your age:',
        initial=0,
        help_text='Enter Your Age',
        widget=forms.NumberInput(), # Default for integer field
    )

    # story = forms.CharField(
    #     widget=forms.Textarea(),
    #     max_length=MAX_LENGTH_STORY,
    # )
    #
    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput(),
    # )
    #
    # secret = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )
    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.Select, # Default for choice field
    )

    # occupancies2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect(),
    # )

    occupancies3 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.SelectMultiple(),
    )
