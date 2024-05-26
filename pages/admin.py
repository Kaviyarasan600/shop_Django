from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Product)
