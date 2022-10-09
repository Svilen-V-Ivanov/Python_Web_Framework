from django.contrib import admin

from django_models.web.models import Employee, NullBlankDemo, Department, Project, Category


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'level', 'department2')
    list_filter = ('level', 'first_name',)
    search_fields = ('first_name', 'last_name')
    sortable_by = ('id', 'first_name')
    fieldsets = (
        (
            'Personal Info',
            {
                'fields': ('first_name', 'last_name', 'age'),
            }
         ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_experience'),
            }
        ),
        (
            'Company Info',
            {
                'fields': ('review', 'department', 'start_date', 'is_full_time', 'email', 'projects')
            }
        )
    )

    def department2(self, obj):
        return obj.department.name


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
