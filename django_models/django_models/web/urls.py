from django.urls import path

from django_models.web.views import index, delete_employee, department_details

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    path('departments/<int:pk>/<slug:slug>/', department_details, name='details department')
)
