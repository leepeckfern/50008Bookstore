"""mysite URL Configuration

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
"""from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login #added
from mysite import views as core_views
from . import views


urlpatterns = [
               #url(r'^polls/', include('polls.urls')),
               
               
               url(r'^accounts/login/',
                   auth_views.login,
                   {
                   'template_name': 'login.html'
                   },
                   name='login'
                   ,),
               url(r'^accounts/logout/',
                   auth_views.logout,
                   {
                   'template_name': 'logout.html'
                   },
                   name='logout'),
               
               url(r'^admin/', admin.site.urls),
               
               url(r'^accounts/signup/',
                   core_views.signup, name='signup'),

               url(r'^search/',
                   core_views.search, name='search'),
               url(r'^$', views.index, name="index")               
               ]
