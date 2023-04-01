from django.contrib import admin
from .models import categoriaProd, producto

# Register your models here.

class categoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductodAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(categoriaProd,categoriaProdAdmin)
admin.site.register(producto,categoriaProdAdmin)
