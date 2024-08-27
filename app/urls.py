from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('', include('type.urls')),
    path('', include('dividend.urls')),
    path('', include('inflows.urls')),
    path('', include('outflow.urls')),
    path('', include('investment.urls')),
]
