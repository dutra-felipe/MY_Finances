from django.contrib import admin
from . import models


class DividendAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_dividends')
    search_fields = ('name', 'total_dividends')


admin.site.register(models.Dividend, DividendAdmin)
