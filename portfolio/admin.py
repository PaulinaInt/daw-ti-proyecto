from django.contrib import admin
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # nombres correctos

admin.site.register(Portfolio, PortfolioAdmin)
