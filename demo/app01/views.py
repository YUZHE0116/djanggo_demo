import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("Hello, World!")
def articcle_year(request,year):
    return HttpResponse("Articles from the year {}".format(year))
def articcle_month(request, year, month):
    return HttpResponse("Articles from {}/{}".format(year, month))
def getdatatime(request):
    today = datetime.date.today()
    format_today=today.strftime("%Y-%m-%d")
    html=f"<h1>今天是{format_today}</h1>"
    return HttpResponse(html)