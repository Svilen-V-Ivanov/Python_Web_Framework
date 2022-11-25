from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('Rest_Demo_2.api.urls')),
    path('', include('Rest_Demo_2.web.urls')),
]
