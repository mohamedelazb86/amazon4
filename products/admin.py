from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product,Review,ImagePOroduct,Brand

class ImgaeAmin(admin.TabularInline):
    model=ImagePOroduct

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','sku','flag']
    list_filter=['brand']
    search_fields=['name','subtitle','descriptions']
    summernote_fields=('subtitle','descriptions')
    inlines=[ImgaeAmin]



admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(ImagePOroduct)