from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from django_models.web.models import Employee, Department


def index(request):
    employees = [x for x in Employee.objects.all() if x.department_id == 2]
    employees2 = Employee.objects.filter(department_id=2) \
        # .order_by('years_of_experience')
    # employees2 = Employee.objects \
    #     .filter(department__name='Engineering') \
    #     .order_by('years_of_experience')
    department = Department.objects.get(pk=2)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug),
    }
    return render(request, 'department-details.html', context)


def delete_employee(request, pk):
    # get_object_or_404(Department, pk=2) \
    #     .delete()
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')
