from django.urls import path, re_path
from .views import helloworld, article_year, article_month, getdatetime

urlpatterns = [
    path('hello/', helloworld),
    path('article/year/<int:year>/', article_year),
    re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})$', article_month),
    path('article/current/', getdatetime),  # Default route
]