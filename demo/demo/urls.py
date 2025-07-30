"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from app01.views import helloworld, articcle_year, articcle_month,getdatatime

urlpatterns = [
    path('',),  # Default route
    path('hello/', helloworld),
    path('articcle/year/<int:year>',articcle_year),
    re_path(r'^articcle/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$',articcle_month),
    path('admin/', admin.site.urls),
    path('articcle/current/', getdatatime),  # Default route
]
