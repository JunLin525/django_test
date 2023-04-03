from django.contrib import admin
from .models import New_table,product

class productadmin(admin.ModelAdmin):
    list_display=('name','qty','price','Available')



admin.site.register(New_table)
admin.site.register(product,productadmin)