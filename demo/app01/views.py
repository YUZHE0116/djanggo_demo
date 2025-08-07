import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello, World!")

def get_current_datetime(request):
    today = datetime.datetime.today()
    format_today = today.strftime("%Y-%m-%d")
    html= "<h1> 当前时间是 %s</h1>" % format_today
    return HttpResponse(html)

    