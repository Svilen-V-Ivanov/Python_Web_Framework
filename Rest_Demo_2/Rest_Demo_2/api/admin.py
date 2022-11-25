from django.contrib import admin

from Rest_Demo_2.api.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
