from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import product
import random

# Create your views here.
def about(request):
   quotes =['an apple a day keeps the doctor away',
            'BTC TO THE MOON',
            'Hello world',
            'hi']
   quote=random.choice(quotes)
   return render(request,'about.html',locals())


def listing(request):
    products=product.objects.all()
    products=product.objects.all().order_by('-qty')
    products2=product.objects.all().filter(qty=0)
    return render(request,'list.html',locals())

def disp_detail(request, sku):
    try:
        p=product.objects.get(sku=sku)
    except product.DoesNotExist:
        raise Http404('找不到你要的品項')
    return render(request,'disp.html', locals())

def mainsite(request):
    return render(request,'mainsite.html')

