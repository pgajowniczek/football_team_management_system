from django.contrib import admin
from .models import StaffFunction, Staff


# Register your models here.

class StaffFunctionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'function', 'club')
    list_display_links = ('name', 'surname')
    list_filter = ('function',)
    search_fields = ('function', 'club', 'surname')


admin.site.register(StaffFunction, StaffFunctionAdmin)
admin.site.register(Staff, StaffAdmin)
