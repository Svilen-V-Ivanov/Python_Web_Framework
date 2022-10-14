from django import forms
from django.shortcuts import render

from forms_examples.web.forms import PersonForm
from forms_examples.web.models import Person


def index_form(request):
    name = None
    if request.method == 'GET':
        form = PersonForm()
    else:
        # request.method == 'post'
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )
        else:
            pass
    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name', 'age')
        # exclude = ('pets', 'name')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            ),
        }
        help_texts = {
            'name': 'Your name',
        }
        labels = {
            'age': 'The Age',
        }


def index_model_form(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save() # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            #
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html', context)
