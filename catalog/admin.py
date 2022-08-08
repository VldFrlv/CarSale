from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price', 'get_photo')
    list_display_links = ('brand', 'model')
    search_fields = ('model', 'brand', 'description')
    readonly_fields = ('views', 'created_at', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo1.url}" width="50">')
        return '-'

admin.site.register(Car)