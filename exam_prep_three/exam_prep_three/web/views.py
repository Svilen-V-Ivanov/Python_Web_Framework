from django.shortcuts import render, redirect

from exam_prep_three.web.forms import ProfileCreateForm, BookCreateForm, BookEditForm, ProfileEditForm, \
    ProfileDeleteForm
from exam_prep_three.web.models import Profile, Book


# Done
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
        'books': Book.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


# Done
def add_book(request):
    profile = get_profile()
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'book/add-book.html', context)


# Done
def edit_book(request, pk):
    book = Book.objects.filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'book/edit-book.html', context)


# Done
def details_book(request, pk):
    book = Book.objects.filter(pk=pk) \
        .get()

    context = {
        'book': book,
    }
    return render(request, 'book/book-details.html', context)


# Done
def delete_book(request, pk):
    book = Book.objects.filter(pk=pk) \
        .get()
    book.delete()
    return redirect('index')


# Done
def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'core/home-no-profile.html', context)


# Done
def details_profile(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }
    return render(request, 'profile/profile.html', context)


# Done
def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)