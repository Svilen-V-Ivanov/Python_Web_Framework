from datetime import date
from enum import Enum

from django.db import models
from django.urls import reverse

from django_models.web.validators import validate_before_today


class AuditInfoMixin(models.Model):

    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True
    )


class Department(AuditInfoMixin ,models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'

    def get_absolute_url(self):
        return reverse('details department', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=15,
        unique=True,
    )
    deadline = models.DateField()

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Employee(AuditInfoMixin, models.Model):

    class Meta:
        ordering = ('years_of_experience', '-age',)

    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
    )
    review = models.TextField()

    years_of_experience = models.PositiveIntegerField()

    start_date = models.DateField(
        validators=(
            validate_before_today,
        )
    )
    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level',
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    email = models.EmailField(
        unique=True,
    )
    age = models.IntegerField(
        default=-1,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'

    @property
    def years_of_employment(self):
        return date.today() - self.start_date


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)

    date_joined = models.DateField(
        auto_now_add=True,
    )


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

# Employee.objects.all()
# Employee.objects.create()
# Employee.objects.filter()
# Employee.objects.update()