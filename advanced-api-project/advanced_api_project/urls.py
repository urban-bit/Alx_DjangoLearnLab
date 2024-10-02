# advanced_api_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Include 'include' for including app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('api/', include('api.urls')),  # Include the API app URLs
]
