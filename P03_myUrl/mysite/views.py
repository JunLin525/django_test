from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def homepage(request):
    return HttpResponse("hello.world")

def about(request,author_no=0):
    html="<h2>Here is NO:{}'s about page!</h2><hr>".format(author_no)
    return HttpResponse(html)

def company(request):
    return HttpResponse("hello.company")

def sales(request):
    return HttpResponse("hello.sales")

def contact(request):
    return HttpResponse("hello.contact")

def listing(request, yr, mon, day):
    html="<h2>This is the list date {}/{}/{}/</h2>".format(yr, mon, day)
    return HttpResponse(html)


def homepage(request):
    yr=2019
    mon=10
    day =30
    post_num=3
    
    html1="<a href='{}'>Show the post link</a><hr><br>"\
        .format(reverse('post-url',args=(yr, mon, day, post_num)))
    
    html2="<a href='{}'>hiiiii</a>"\
        .format(reverse('list-url', args=(yr, mon, day)))
    html=html1+html2
    return HttpResponse(html)
    

def post(request, yr, mon, day, post_num):
    html="<h2>Today is {}/{}/{} : your post number:{}</h2><hr>".format(yr, mon, day, post_num)
    return HttpResponse(html)