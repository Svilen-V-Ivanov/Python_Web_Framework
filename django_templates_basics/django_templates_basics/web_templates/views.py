from datetime import datetime
from random import random

from django.http import HttpResponse
from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}; Age: {self.age}"


def index(request):
    context = {
        'title': "sample Homepage",
        'value': random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student('Doncho', 19),
        'student_info': Student('Doncho', 19).get_info(),
        'current_time': datetime.now(),
        'students': ['Pesho', 'Pesho','Gosho','Maria','Stamat'],
        #'students': [],
        'values': list(range(20)),
    }

    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
