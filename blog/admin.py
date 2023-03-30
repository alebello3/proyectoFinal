from django.contrib import admin
from.models import categoria, post
# Register your models here.


class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categoria, categoriaAdmin)
admin.site.register(post, PostAdmin)