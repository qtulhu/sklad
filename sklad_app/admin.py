from django.contrib import admin
from .models import sklad_item

# admin.site.register(sklad_item)
@admin.register(sklad_item)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name','many', 'how_many', 'serial_number', 'mac', 'create_time', 'status', 'given_time', 'receiver')
    list_filter = ('type','status', 'receiver', 'name')
    search_fields = ('name', 'receiver')
    date_hierarchy = 'create_time'
    ordering = ('status', 'create_time','given_time')
