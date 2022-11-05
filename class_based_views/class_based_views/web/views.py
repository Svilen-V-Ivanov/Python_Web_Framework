import random

from django import forms
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from class_based_views.web.models import Employee


def index(request):
    context = {
        'title': 'FBV'
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class BV'
        }
        return render(request, 'index.html', context)

    def posst(self, request):
        pass

    # In Django Rest Framework
    # def put(self, request):
    #     pass


class IndexViewTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Template view',
    } # static context

    # Dynamic context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'
    extra_context = {
        'title': 'ListView',
    }

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern)
        # queryset = queryset.order_by('first_name')
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class EmployeeDetailsView(views.DetailView):
    context_object_name = 'employee' # renames 'object' to 'employees'
    model = Employee
    template_name = 'details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter name',
                }
            ),
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'create.html'
    model = Employee
    fields = '__all__'
    # success_url = '/' # static 'success_url'

    # Dynamic
    def get_success_url(self):
        return reverse_lazy('employee details', kwargs={
            'pk': self.object.pk,
        })
    # Replace automatic form
    # form_class = EmployeeCreateForm

    # Change the automatic form
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = 'Enter ' + name
    #
    #     return form


class RedirectToDetailsMixin:
    url_name = None

    def get_url_kwargs(self):
        return {}

    def get_success_url(self):
        return reverse_lazy(
            self.url_name,
            kwargs=self.get_url_kwargs(),
            )


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     result = reverse_lazy('employee details', kwargs={
    #         'pk': self.object.pk,
    #     })
    #
    #     return result

# Alternative
# class EmployeeUpdateView(RedirectToDetailsMixin, views.UpdateView):
#     model = Employee
#     fields = '__all__'
#     template_name = 'create.html'
#
#     url_name = 'employee details'
#
#     def get_url_kwargs(self):
#         return {
#             'pk': self.object.pk,
#         }
# def get_view(request):
#     handler = None
#     if request.method == 'GET':
#         handler = self.get
#     else:
#         handler = self.post
#     return handler()


# class IndexView:
#     def __init__(self):
#         self.values = [
#             random.randint(1, 15),
#         ]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It Works! : {self.values}')
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))




