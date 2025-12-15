from django.contrib import admin
from django.urls import path, include
from tracker.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')), 
    path('', dashboard_view, name='dashboard'),
]
