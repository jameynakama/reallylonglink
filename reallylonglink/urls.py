"""reallylonglink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from reallylonglink import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(r'', views.HomeView.as_view(), name='home'),
    path('reallylonglink/<int:pk>/', views.generated_link_view, name='generated_link'),
    re_path(r'^{}/(?P<long_link>[{}]+)/$'.format(settings.BASE_REDIRECT_URL,
                                                 settings.LINK_CHARS),
            views.RLLRedirectView.as_view(), name='redirect'),
]
