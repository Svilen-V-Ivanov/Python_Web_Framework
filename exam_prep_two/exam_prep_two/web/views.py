from django.shortcuts import render, redirect

from exam_prep_two.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from exam_prep_two.web.models import Profile, Game


def get_average_ranking():
    games = Game.objects.all()
    if len(games) == 0:
        return 0.0
    average = 0
    for game in games:
        average += game.rating
    average = average / len(games)

    return average


# Done
def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


# Done
def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


# Done
def create_profile(request):
    profile = get_profile()
    if profile:
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
    return render(request, 'profile/create-profile.html', context)


# Done
def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'core/dashboard.html', context)


# Done
def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


# Done
def details_game(request, pk):
    game = Game.objects.filter(pk=pk) \
        .get()

    context = {
        'game': game,
    }
    return render(request, 'game/details-game.html', context)


# Done
def edit_game(request, pk):
    game = Game.objects.filter(pk=pk) \
        .get()
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/edit-game.html', context)


# Done
def delete_game(request, pk):
    game = Game.objects.filter(pk=pk) \
        .get()
    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/delete-game.html', context)


# Done
def details_profile(request):
    profile = get_profile()
    games_count = Game.objects.count()
    name = None
    if profile.first_name or profile.last_name:
        if profile.first_name and profile.last_name:
            name = f"{profile.first_name} {profile.last_name}"
        elif profile.first_name:
            name = f"{profile.first_name}"
        elif profile.last_name:
            name = f"{profile.last_name}"
    average = get_average_ranking()
    context = {
        'profile': profile,
        'games_count': games_count,
        'name': name,
        'average': average,
    }

    return render(request, 'profile/details-profile.html', context)


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
        'form': form,
    }
    return render(request, 'profile/delete-profile.html', context)

