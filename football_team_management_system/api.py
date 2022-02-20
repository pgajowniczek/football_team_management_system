from rest_framework import routers
from team.api_views import ClubViewset, PlayerViewset, WageViewset, CurrencyViewset, ExchangeRateViewset, InjuryViewset
from league.api_views import RefereeFunctionViewset, RefereeViewset, StadiumViewset, GameViewset, ActionViewset, \
    CourseOfTheGameViewset, LeagueViewset
from training_staff.api_views import StaffFunctionViewset, StaffViewset
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'clubs', ClubViewset)
router.register(r'players', PlayerViewset)
router.register(r'wages', WageViewset)
router.register(r'referee_functions', RefereeFunctionViewset)
router.register(r'referees', RefereeViewset)
router.register(r'stadiums', StadiumViewset)
router.register(r'games', GameViewset)
router.register(r'actions', ActionViewset)
router.register(r'game_courses', CourseOfTheGameViewset)
router.register(r'staff_functions', StaffFunctionViewset)
router.register(r'staffs', StaffViewset)
router.register(r'leagues', LeagueViewset)
router.register(r'currencies', CurrencyViewset)
router.register(r'exchange_rates', ExchangeRateViewset)
router.register(r'injuries', InjuryViewset)

# DRF-Nested-Routers - test
players_in_team_router = routers.NestedSimpleRouter(router, r'clubs', lookup='club')
players_in_team_router.register(r'players', PlayerViewset)