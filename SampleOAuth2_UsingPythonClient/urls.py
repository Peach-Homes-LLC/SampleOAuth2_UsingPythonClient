"""SampleOAuth2_UsingPythonClient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.urls import include, re_path
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    re_path(r'^$', RedirectView.as_view(pattern_name='app:index')),
    re_path(r'^app/', include('app.urls', namespace='app')),
    re_path(r'^admin/', admin.site.urls),
]
