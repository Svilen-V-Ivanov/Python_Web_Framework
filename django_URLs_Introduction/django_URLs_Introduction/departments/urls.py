from django.urls import path

from django_URLs_Introduction.departments.views import show_departments, show_department_details, \
    show_departments_with_render, redirect_to_first_department, show_not_found

urlpatterns = (
    path('', show_departments, name='show departments'),
    path('not-found/', show_not_found, name='not found'),
    path('redirect/', redirect_to_first_department, name='redirect test'),
    path('<department_id>/', show_department_details, name='show departments with string'),
    path('int/<int:department_id>/', show_departments_with_render, name='show departments with html'),

)
