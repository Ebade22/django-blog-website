from django.contrib import admin
from .models import BlogPost

# Register your models here.
class MainAppAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "published_date"]
    list_display_links = ['id','title']

admin.site.register(BlogPost, MainAppAdmin)

admin.site.site_header = "Ebades Blog Panel"
admin.site.site_title = "Admin Panel"