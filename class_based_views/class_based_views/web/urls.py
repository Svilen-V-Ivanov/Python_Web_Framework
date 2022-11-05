from django.urls import path
from django.views import generic as views
from class_based_views.web.views import IndexView, IndexViewTemplate, IndexViewWithListView, EmployeeDetailsView, \
    EmployeeCreateView, EmployeeUpdateView

the_view = IndexView.as_view()
print(the_view)
urlpatterns = (
    path('', IndexViewWithListView.as_view(), name='index'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
    path('redirect-to-index/', views.RedirectView.as_view(url='/'), name='redirect to index'),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee update'),
)
