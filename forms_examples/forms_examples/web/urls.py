from django.urls import path

from forms_examples.web.views import index_form, index_model_form

urlpatterns = (
    path('', index_form, name='index'),
    path('modelforms/', index_model_form, name='model index'),
)
