from django.contrib import admin

from apps.base.models import NavigationLog


@admin.register(NavigationLog)
class NavigationLogAdmin(admin.ModelAdmin):
    list_display = ('url', 'timestamp')
    list_filter = ('url', 'timestamp')
    search_fields = ('url', 'timestamp')
    ordering = ('-timestamp',)
