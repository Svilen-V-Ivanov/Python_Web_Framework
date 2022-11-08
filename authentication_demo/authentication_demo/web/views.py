from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic as views
from django.shortcuts import render

from django.contrib.auth.models import User

from authentication_demo.web.decorators import allow_groups


# Function based view - required log-in
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse(f'You are {request.user}')


# Class based views - required log-in
class ProfileView(LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f'You are {request.user.username}')


# @allow_groups
@allow_groups(groups=['Users'])
def index(request):
    # print(
    #     authenticate(username='doncho', password='dOn4o$min'),
    #     authenticate(username='gosho', password='!passwOr4#'),
    #     authenticate(username='gosho', password='!pas22Or4#'),
    #     authenticate(username='theshadowtm', password='1password2'),
    # )
    # new_user = User.objects.create_user(
    #     username='doncho',
    #     password='dOn4o$min',
    #     first_name='Doncho',
    #     last_name='Minkov',
    # )
    # print(request.user)
    user_message = '' if request.user.is_authenticated else ' not'
    return HttpResponse(f'The user is{user_message} authenticated')


def permissions_debug(request):
    usernames = {
        'doncho',
        'gosho',
        # 'Maria',
        'theshadowtm'}
    users = User.objects.filter(username__in=usernames)
    # list of permissions(not just these, there are more)
    permissions_to_check = ['auth.add_user', 'auth.change_user', 'auth.delete_user', 'auth.view_user']
    for user in users:
        print('-' * 30)
        print(f'User: {user}')
        print(f'Has {permissions_to_check}')
        # Check if user has any permission from a list
        for perm in permissions_to_check:
            print(user.has_perm(perm))
        # Checks if user has all permissions from a list
        print(user.has_perms(permissions_to_check))

    return HttpResponse('It works')


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Maria',
        password='User.objects.create_',
    )

    # -creates the session
    # -attaches 'user' to request
    login(request, user)
    print(request.user)

'''
gosho
!passwOr4#
'''