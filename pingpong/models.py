from django.db import models
from django.db.models import F, Sum


class Player(models.Model):
    name = models.CharField(max_length=64)

    def get_wins(self):
        return (
            self.participations
                .filter(points__gt=F('other_participation__points'))
                .count()
        )

    def get_total_points_earned(self):
        return self.participations.aggregate(Sum('points'))

    def get_total_points_allowed(self):
        return self.participations.aggregate(Sum('other_participation__points'))


class Game(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)


class Participation(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name='participations'
    )
    points = models.PositiveIntegerField()
    other_participation = models.OneToOneField(
        'self',
        on_delete=models.CASCADE,
        related_name='+'
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.other_participation.other_participation = self
        super(Participation, self.other_participation).save()
