from django.contrib import admin
from mysite import models as mysite_models
# Register your models here.

admin.site.register(mysite_models.Maker)
admin.site.register(mysite_models.PModel)
admin.site.register(mysite_models.Product)
admin.site.register(mysite_models.PPhoto)