from django.contrib import admin
from .models import Category, Place

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'rating')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'address', 'phone', 'siteurl', 'rating')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}    

admin.site.register(Category, CategoryAdmin)    
admin.site.register(Place, PlaceAdmin)    
