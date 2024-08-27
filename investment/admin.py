from django.contrib import admin
from . import models


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'investment_type', 'operation', 'amount', 'quantity')
    search_fields = ('name', 'symbol', )


admin.site.register(models.Investment, InvestmentAdmin)
