"""authors URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .apps.articles import urls

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
        name='admin'),
    path(
        'api/',
        include('authors.apps.authentication.urls'),
        name='authentication'),
    path(
        'api/',
        include('authors.apps.profiles.urls'),
        name='profiles'),
    path(
        'api/profile/',
        include('authors.apps.profiles.urls'),
        name='profile'),
    path(
        'api/articles/', include(urls),
        name='all_articles'),
]
