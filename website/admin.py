from django.contrib import admin

from .models import Category, Part, Name, Inventory, Log

# Register your models here.
class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')

class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'part', 'name')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'part', 'category',)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'part', 'name', 'quantity', 'price',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'part', 'name', 'quantity', 'price',)
    
admin.site.register(Name, NameAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Log, LogAdmin)
