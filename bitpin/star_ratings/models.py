from __future__ import division, unicode_literals

from decimal import Decimal
from multiprocessing.spawn import import_main_path
from operator import imod

from django.conf import settings
from django.db import models
from django.db.models import Avg, Count
from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from contents.models import Content


class Rating(models.Model):
    """
    Attaches Rating models and running counts to the model being rated
    """
    count = models.PositiveBigIntegerField(default=0)
    average = models.DecimalField(max_digits=6, decimal_places=3, default=Decimal(0.0))
    content = models.OneToOneField(Content, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"id:{self.content.id} — title:{self.content.title}"

    def calculate(self):
        """
        Recalculate and save.
        """
        aggregates = self.user_ratings.aggregate(average=Avg('score'), count=Count('score'))
        self.count = aggregates.get('count') or 0
        self.average = aggregates.get('average') or 0.0
        self.save()


class UserRating(models.Model):
    """
    An individual rating of a user against Content model.
    """
    SCORE_CHOICES = (
        (1, _("Terrible")),
        (2, _("Poor")),
        (3, _("Average")),
        (4, _("Very Good")),
        (5, _("Excellent")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES, default=1, 
            validators=[
                MaxValueValidator(5),
                MinValueValidator(1)
            ]
    )
    rating = models.ForeignKey(Rating, related_name='user_ratings', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(UserRating, self).save(*args, **kwargs)
        if int(self.score) < 1 or int(self.score) > 5:
            raise ValidationError('Score must be located between 0 to 5')

    class Meta:
        unique_together = ['user', 'rating']

    def __str__(self):
        if not settings.STAR_RATINGS_ANONYMOUS:
            return '{} rating {} for {}'.format(self.user, self.score, self.rating.content)
        return '{} rating {} for {}'.format(self.score, self.rating.content)
