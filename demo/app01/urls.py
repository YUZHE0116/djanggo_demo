from django.urls import path
from .import views
urlpatterns = [
    path('hello/', views.helloworld),
    path('current/', views.get_current_datetime),
    # 在这里添加你的路由
]