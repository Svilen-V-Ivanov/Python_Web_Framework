import random
from time import sleep

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views import generic as views

from common_web_tools.web.models import Employee

CLICKS_COUNT_SESSION_KEY = 'CLICKS_COUNT_SESSION_KEY'
LATEST_VALUE_SESSION_KEY = 'LATEST_VALUE_SESSION_KEY'

UserModel = get_user_model()


def very_slow_operation():
    sleep(2)
    return random.randint(1, 1024)


# @cache_page(1 * 60)
def index(request):
    Employee.objects.create(
        first_name='Doncho',
        last_name='Peshov',
        age=27,
    )
    value = very_slow_operation()
    latest_values = request.session.get(LATEST_VALUE_SESSION_KEY, [])
    latest_values = [value] + latest_values
    latest_values = latest_values[:3]
    request.session[LATEST_VALUE_SESSION_KEY] = latest_values

    return HttpResponse(f'Value: {value}; Latest: {", ".join(str(x) for x in latest_values)}')


def show_session(request):
    clicks_count = request.session.get(CLICKS_COUNT_SESSION_KEY, 0) + 1
    request.session[CLICKS_COUNT_SESSION_KEY] = clicks_count

    return HttpResponse(f'Clicks: {clicks_count}')


def raise_error(request):
    UserModel.objects.get(pk=100010)


class EmployeesListView(views.ListView):
    model = Employee
    template_name = 'employees/list.html'
    default_paginate_by = 3

    # paginate_by = 3

    def get_paginate_by(self, queryset):
        return self.request.GET.get('page_size', self.default_paginate_by)

# for i in range(10):
#     Employee.objects.create(
#         first_name=f'Doncho {i + 1}',
#         last_name=f'Minkov {i + 1}',
#         age=22,
#         user_id=i+3,
#     )
#     UserModel.objects.create_user(
#         username=f'doncho-{i + 1}',
#         password='opi5$stf32*',
#     )