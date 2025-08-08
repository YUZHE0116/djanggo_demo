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
def list(request):
    authors = 'yuzhe'
    article_number = 10
    article_list = [
        'Django入门', 
        'Django是一个高级的Python Web框架。',
        'Django的设计'
        ]
    info = {'name':'zhuyu'
            ,'age':18
            ,'programming_language':['Python', 'Java', 'C++']
            }
    return render(request, 'list.html',{
        'authors': authors,
        'article_number': article_number,
        'article_list': article_list
        ,'info': info
        })

    