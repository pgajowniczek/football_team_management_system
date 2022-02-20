from django.db import models
#from team.models import Club


# staff function (coach, physiotherapist, etc.):
class StaffFunction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    function = models.ForeignKey(StaffFunction, on_delete=models.CASCADE)
    club = models.ForeignKey('team.Club', on_delete=models.CASCADE)
