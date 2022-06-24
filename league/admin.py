from django.contrib import admin
from .models import Referee, Game, Stadium, RefereeFunction, Action, CourseOfTheGame, League


class RefereeAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'function')
    list_filter = ('surname',)
    search_fields = ('surname', 'function')
    list_per_page = 10


class GameAdmin(admin.ModelAdmin):
    list_display = ('home', 'away', 'stadium', 'referee')
    list_display_links = ('home', 'away', 'stadium', 'referee')
    list_filter = ('stadium',)
    search_fields = ('stadium', 'home', 'away')
    list_per_page = 10


class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'street', 'post_code', 'number', 'city')
    list_filter = ('city',)
    search_fields = ('city', 'name')
    list_per_page = 10


class RefereeFunctionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ActionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CourseOfTheGameAdmin(admin.ModelAdmin):
    list_display = ('minute', 'what_happened', 'player', 'game')
    list_display_links = ('game', 'player')
    list_filter = ('game',)


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


admin.site.register(Referee, RefereeAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Stadium, StadiumAdmin)
admin.site.register(RefereeFunction, RefereeFunctionAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(CourseOfTheGame, CourseOfTheGameAdmin)
admin.site.register(League, LeagueAdmin)
