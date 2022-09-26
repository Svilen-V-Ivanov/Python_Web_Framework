from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, resolve_url

# Create your views here.


def show_departments(request: HttpRequest, *args, **kwargs):
    #print(request.GET)
    #print(request.method)
    #print(request.get_port())
    #print(request.headers)
    order_by = request.GET.get('order_by', 'name')
    sample = f' path = {request.path}, args = {args}, kwargs = {kwargs}, order_by = {order_by}'
    return HttpResponse(sample)


def show_department_details(request: HttpRequest, department_id):
    sample = f' path = {request.path}, details = {department_id}'
    return HttpResponse(sample)


def show_departments_with_render(request: HttpRequest, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }

    return render(request, 'departments/all.html', context)


def redirect_to_first_department(request):
    possible_order = ['name', 'age', 'id']
    order_by = choice(possible_order)
    #path = f'/departments/int/1/?order_by={order_by}'
    #path = 'http://softuni.bg'
    return redirect('show departments with html', department_id=5)


def show_not_found(request):
    status_code = 400
    #return HttpResponseNotFound('Page Not Found')
    #return HttpResponse("Error", status=status_code)
    raise Http404("Not found!!!")
