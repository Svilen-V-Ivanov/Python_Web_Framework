from django.urls import path

from common_web_tools.web.views import index, show_session, raise_error, EmployeesListView

urlpatterns = (
    path('', index, name='index'),
    path('sessions/', show_session, name='sessions'),
    path('error/', raise_error, name='raise error'),
    path('employees/', EmployeesListView.as_view(), name='employee list'),
)

from .signals import *