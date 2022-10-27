from django.urls import path, include

from exam_prep_three.web.views import index, add_book, edit_book, details_book, details_profile, edit_profile, \
    delete_profile, add_profile, delete_book

urlpatterns = (
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', include([
        path('', details_profile, name='details profile'),
        path('add/', add_profile, name='add profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete', delete_profile, name='delete profile'),
    ]))
)
