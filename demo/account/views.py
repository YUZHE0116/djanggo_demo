from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse(f"用户名：{username}, 密码：{password}")
    elif request.method == "GET":
        FORBIDDEN_IP= ['127.0.0.1']
        print(request.META.get('REMOTE_ADDR'))
        if request.META.get('REMOTE_ADDR') in FORBIDDEN_IP:
            return HttpResponse("禁止访问")
        return render(request, 'login.html')
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        return HttpResponse(f"注册成功！用户名：{username}, 密码：{password}")

