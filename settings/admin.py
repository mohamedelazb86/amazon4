from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Setting


class SettinAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','email_us']
    
    search_fields=['name','subtitle']

    summernote_fields = ('subtitle',)

admin.site.register(Setting,SettinAdmin)
