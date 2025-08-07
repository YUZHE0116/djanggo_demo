from django.urls import path
from . import views

urlpatterns = [
    # 在这里添加你的URL模式，例如：
   path('login/', views.login_view, name='login'),
]