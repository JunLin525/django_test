from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from .models import Post
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now
    html = template.render(locals())
    #post_lists =list()
    #for count, post in enumerate(posts):
    #    post_lists.append("No.{}:".format(str(count)) +str(post)+str(' ')+str(post.pub_date)+"<br>")
    #    post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    return HttpResponse(html)

def showpost(request, slug):
    template=get_template('post.html')
    now = datetime.now
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
    

def listing(request, yr, mon, day):
    html="<h2>You List Date is {}/{}/{}</h2><hr>".format(yr, mon, day)
    return HttpResponse(html)

def post(request, yr, mon, day, post_num):
    html="<h2>Today is {}/{}/{}: Your Post Number is {}</h2><hr>".format(yr,mon,day,post_num)
    return HttpResponse(html)