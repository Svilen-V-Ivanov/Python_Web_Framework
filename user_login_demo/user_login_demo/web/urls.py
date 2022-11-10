from django.urls import path

from user_login_demo.web.views import UsersListView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
)