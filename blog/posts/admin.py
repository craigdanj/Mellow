from django.contrib import admin
from .models import Category, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'pub_date')
	list_filter = ['category', 'tag']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
