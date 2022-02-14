"""tdd2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin

from django.urls import re_path, include, path

# from django.conf.urls.static import static - Don't need to import static

from . import views

urlpatterns = [
    # re_path(route, view, kwargs=None, name=None)
    re_path(r'^admin/', admin.site.urls), # pass admin.stie.urls directly. No need include
    re_path(r'^$', views.HomeView.as_view(), name='home'), # Use regex and re_path

    # re_path uses regex, path use just <slug:title>.

    # path('admin/', admin.site.urls), # pass admin.stie.urls directly. No need include
    # path('', views.HomeView.as_view(), name='home'), # Use regex
]
