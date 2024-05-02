from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product,Review,ImagePOroduct,Brand

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','sku','flag']
    list_filter=['brand']
    search_fields=['name','subtitle','descriptions']
    summernote_fields=('subtitle','descriptions')



admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(ImagePOroduct)