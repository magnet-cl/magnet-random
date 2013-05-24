from django.contrib import admin

from randomizer.models import Name


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')

admin.site.register(Name, NameAdmin)
