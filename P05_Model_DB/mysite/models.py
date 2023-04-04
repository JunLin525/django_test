from django.db import models

# Create your models here.
class Maker(models.Model):
    name=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class PModel(models.Model):
    maker=models.ForeignKey(Maker, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    url=models.URLField(default='http://i.imgur.com/Ous4iGB.png')
    str:str
    def __str__(self):
        return self.name

class Product(models.Model):
    pmodel=models.ForeignKey(PModel,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=50,default='超值二手機')
    discription=models.TextField(default='沒有說明')
    Year=models.PositiveIntegerField(default=2016)
    price=models.PositiveIntegerField(default=0)
    qty=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname
    
class PPhoto(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    dispcription=models.CharField(max_length=20,default='產品照片')
    url=models.URLField(default='http://i.imgur.com/Z230eeq.png')

    def __str__(self):
        return self.dispcription