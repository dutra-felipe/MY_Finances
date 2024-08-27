from django.contrib import admin
from . import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('asset', 'quantity', 'amount', 'created_at', 'updated_at', )
    search_fields = ('asset__name', )


admin.site.register(models.Outflow, OutflowAdmin)
