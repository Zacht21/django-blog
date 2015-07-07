from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

class EntradaAdmin(MarkdownModelAdmin):
    list_display = ("titulo", "creado")
    prepopulated_fields = {"slug": ("titulo",)}

admin.site.register(models.Entrada, EntradaAdmin)