from django.shortcuts import render, get_object_or_404
from mysite import models
# Create your views here.

def index(request):
    products=models.Product.objects.all()
    return render(request, 'index.html', locals())

def detail(request, id):
    try:
        product=models.Product.objects.get(id=id)
        images=models.PPhoto.objects.filter(product=product)
    except models.Product.DoesNotExist:
        product = None
    return render(request,'detail.html',locals())
