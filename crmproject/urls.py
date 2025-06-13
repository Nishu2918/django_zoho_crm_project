from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crmleads/', include('crmleads.urls')),  # <-- This line is correct
]
