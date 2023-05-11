from django.contrib import admin

from .models import Category, Subcategory, Part, Inventory, Log

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)

class SubAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'category',)

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subcategory', 'price',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'subcategory', 'quantity', 'price',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'subcategory', 'quantity', 'price', 'time',)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Log, LogAdmin)
