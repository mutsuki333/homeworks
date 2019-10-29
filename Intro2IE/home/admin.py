from django.contrib import admin
from django.apps import apps
from django.contrib.auth.models import Group

admin.site.site_header = '庫存後台管理'
admin.site.unregister(Group)


from .models import Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','stock','description','picture')