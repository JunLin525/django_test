from django.shortcuts import render
from django.http import HttpResponse
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