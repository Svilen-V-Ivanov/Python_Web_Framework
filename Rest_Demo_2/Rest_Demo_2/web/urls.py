from django.urls import path

from Rest_Demo_2.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
