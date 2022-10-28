from django.shortcuts import render, redirect

from exam_prep_four.web.forms import CreateProfile, CreateNote, EditNote, DeleteNote
from exam_prep_four.web.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


# Done
def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'profile': profile,
        'notes': Note.objects.all(),
    }
    return render(request, 'core/home-with-profile.html', context)


# Done
def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = CreateProfile()
    else:
        form = CreateProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


# Done
def add_note(request):
    if request.method == 'GET':
        form = CreateNote()
    else:
        form = CreateNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'note/note-create.html', context)


# Done
def edit_note(request, pk):
    note = Note.objects.filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = EditNote(instance=note)
    else:
        form = EditNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note/note-edit.html', context)


# Done?
def delete_note(request, pk):
    note = Note.objects.filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = DeleteNote(instance=note)
    else:
        form = DeleteNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note/note-delete.html', context)


# Done
def details_note(request, pk):
    note = Note.objects.filter(pk=pk) \
        .get()
    context = {
        'note': note,
    }
    return render(request, 'note/note-details.html', context)


def profile(request):
    profile = get_profile()
    notes_count = Note.objects.all().count()
    context = {
        'profile': profile,
        'notes_count': notes_count
    }
    return render(request, 'profile/profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if profile is None:
        return redirect('index')

    note = Note.objects.all()

    profile.delete()
    note.delete()
    return redirect('index')
