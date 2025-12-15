from django.contrib import admin
from .models import Language


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'date_added']
    list_filter = ['category', 'proficiency']
    search_fields = ['name', 'description']
    ordering = ['-date_added']
