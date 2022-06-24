from django.contrib import admin
from .models import Player, Club, Currency, ExchangeRate, Wage, Injury
from django.utils.text import Truncator


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'shirt_number', 'team', 'email')
    list_display_links = ('surname', 'name')
    list_filter = ('surname', 'team', 'shirt_number')
    search_fields = ('surname', 'team', 'shirt_number')
    list_per_page = 10


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded', 'league')
    list_display_links = ('name',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'currency_shortcut')


class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('exchange_rate', 'currency')


class WageAdmin(admin.ModelAdmin):
    list_display = ('wage', 'currency', 'start', 'end', 'player')
    list_display_links = ('wage',)
    list_filter = ('player',)
    search_fields = ('player',)
    list_per_page = 10


def part_of_description(obj):
    descr = f"{obj.description}"
    return Truncator(descr).chars(50)


class InjuryAdmin(admin.ModelAdmin):
    list_display = ('player', 'start_date', 'end_date', part_of_description, 'main_doctor')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate, ExchangeRateAdmin)
admin.site.register(Wage, WageAdmin)
admin.site.register(Injury, InjuryAdmin)
