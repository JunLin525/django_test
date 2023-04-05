from django.contrib import admin
from mysite import models as mysite_models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','pmodel','nickname','price','year')
    search_fields=('description','pmodel','nickname','price','year')
    ordering=('-price',)

class PPhotoAdmin(admin.ModelAdmin):
    list_display=('product','dispcription','url',)
    ordering=('id',)

admin.site.register(mysite_models.Maker)
admin.site.register(mysite_models.PModel)
admin.site.register(mysite_models.Product,ProductAdmin)
admin.site.register(mysite_models.PPhoto,PPhotoAdmin)