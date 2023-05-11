from django.contrib import admin

from .models import Category, Part, Inventory, Log

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'quantity', 'price',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'quantity', 'price', 'time',)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Log, LogAdmin)
