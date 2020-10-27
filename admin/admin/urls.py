from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
