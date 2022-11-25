from django.views import generic as views
from rest_framework import generics as rest_views, views as rest_base_views, viewsets
from rest_framework.response import Response
from Rest_Demo_2.api.models import Employee, Department
from Rest_Demo_2.api.serializers import DepartmentSerializer, EmployeeSerializer, DemoSerializer


# Server-side rendering, i.e result is rendered HTML
class EmployeesListView(views.ListView):
    model = Employee
    template_name = ''


class DepartmentsListApiView(rest_views.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# JSON serialization, i.e parse models into JSON
class EmployeesListApiView(rest_views.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        queryset = self.queryset
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset.all()


class DemoApiView(rest_base_views.APIView):
    def get(self, request):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        body = {
            'employees': employees,
            'employees_count': employees.count(),
            'departments': departments,
            'first_department': departments.first(),
            'department_names': departments,
        }

        serializer = DemoSerializer(body)

        # Not 'HttpResponse' -from **Django**
        # Response comes from **DRF**
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    