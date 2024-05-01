from django.contrib import admin
from .models import Post,Review,Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display=['user','title','draft']
    list_filter=['draft']
    search_fields=['content','title']

    summernote_fields = ('content',)

    


admin.site.register(Post,PostAdmin)
admin.site.register(Review)
admin.site.register(Category)

