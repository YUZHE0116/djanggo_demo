from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login),
    # 在这里添加你的URL模式
]