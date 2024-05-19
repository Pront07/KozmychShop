from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'index')
    list_editable = ('is_active', 'index')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'content')
        }),
        ('Додатково', {
            'classes': ('collapse',),
            'fields': ('is_active', 'index')
        }),
    )
    save_on_top = True
    save_as = True
    save_as_continue = True
    save_on_top = True
    save_on_bottom = True