from django.urls import path
from . import views

urlpatterns = [
    path('team/players', views.TeamList.as_view())
]