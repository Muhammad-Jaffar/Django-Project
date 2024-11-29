"""
URL configuration for LearnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# marketplace/marketplace/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from accounts.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home_view, name='home'),
    # Add placeholders for future dashboards
    path('seller/', include([
        path('dashboard/', lambda request: render(request, 'seller/dashboard.html'), name='seller_dashboard'),
    ])),
    path('buyer/', include([
        path('dashboard/', lambda request: render(request, 'buyer/dashboard.html'), name='buyer_dashboard'),
    ])),
]

# Add media and static file serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
