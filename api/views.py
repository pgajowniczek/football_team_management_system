from rest_framework import generics, permissions
from .serializers import TeamSerializer
from team.models import Player


class TeamList(generics.ListAPIView):
    serializer_class = TeamSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        return Player.objects.order_by('shirt_number')
