from django.contrib import admin

from .models import Category, Type, Part, Inventory, Log

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'category',)

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'type',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'part', 'type', 'quantity', 'price',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'part', 'type', 'quantity', 'price', 'time',)
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Log, LogAdmin)
