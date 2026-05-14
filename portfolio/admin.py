from django.contrib import admin
from .models import Portfolio, Tarea

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "enlace", "created", "updated")
    search_fields = ("title", "description")
    list_filter = ("created", "updated")
    readonly_fields = ("created", "updated")

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "archivo")
