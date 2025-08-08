from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # return HttpResponse(f"用户名：{username}, 密码：{password}")
        res = {
            "name": username, 
            "password": password
            }
        return JsonResponse(res)
    elif request.method == "GET":
        FORBIDDEN_IP= []
        print(request.headers.get('User-Agent'))
        # print(request.META.get('REMOTE_ADDR'))
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

