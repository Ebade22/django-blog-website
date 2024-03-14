from django.contrib import admin
from .models import BlogPost,Category,Tag
# Register your models here.


class MainAppAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'published_date']
    list_display_links=['id', 'title']

admin.site.register(BlogPost, MainAppAdmin)
admin.site.register(Category)
admin.site.register(Tag)

admin.site.site_header="Ebade Blog Website Panel"
admin.site.index_title="Administration Panel"
admin.site.site_title="Administration Panel"