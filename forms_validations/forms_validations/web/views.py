from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_validations.web.forms import TodoCreateForm, TodoForm, PersonCreateForm
from forms_validations.web.models import Person
from forms_validations.web.validators import validate_text, validate_priority, ValueInRangeValidator


def index(request):
    # validate_text('Sample text_')
    form_class = TodoForm
    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)

        if form.is_valid():
            # model = form.instance
            # model.full_clean()
            # form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-person.html', context)


def create_person(request):
    if request.method == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)