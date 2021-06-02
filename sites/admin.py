from django.contrib import admin
from .models import Post, Traffic

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "views"]

class TrafficAdmin(admin.ModelAdmin):
    list_display = ['post', 'date', 'country', 'region']

admin.site.register(Post, PostAdmin)
admin.site.register(Traffic, TrafficAdmin)