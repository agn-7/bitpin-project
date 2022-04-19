from decimal import Decimal

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models import Avg


SCORE_CHOICES = (
    (1, _("Terrible")),
    (2, _("Poor")),
    (3, _("Average")),
    (4, _("Very Good")),
    (5, _("Excellent")),
)
SCORE_CHOICES2 = (
    ("1", _("Terrible")),
    ("2", _("Poor")),
    ("3", _("Average")),
    ("4", _("Very Good")),
    ("5", _("Excellent")),
)


class OverallStarRating(models.Model):
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_id")

    average_rating = models.FloatField(
        verbose_name=_("Average rating"),
        default=0,
    )
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES,
    )

    # objects = OverallRatingStarManager()  # TODO

    class Meta:
        unique_together = [
            ("object_id", "content_type", "score"),
        ]

    def update(self):
        r = (
            StarRating.objects.filter(overall_score=self).aggregate(
                r=Avg("average_rating")
            )["r"]
            or 0
        )
        self.score = Decimal(str(r))
        self.save()


class StarRating(models.Model):
    overall_score = models.ForeignKey(
        OverallStarRating, null=True, related_name="ratings", on_delete=models.CASCADE
    )
    object_id = models.PositiveIntegerField(db_index=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    average_rating = models.IntegerField()
    score = models.CharField(max_length=250, blank=True, choices=SCORE_CHOICES2)

    def clear(self):
        overall = self.overall_score
        self.delete()
        overall.update()
        return overall.rating

    @classmethod
    def update(cls, rating_object, user, rating, category=""):
        ct = ContentType.objects.get_for_model(rating_object)
        rating_obj = cls.objects.filter(
            object_id=rating_object.pk, content_type=ct, user=user, category=category
        ).first()

        if rating_obj and rating == 0:
            return rating_obj.clear()

        if rating_obj is None:
            rating_obj = cls.objects.create(
                object_id=rating_object.pk,
                content_type=ct,
                user=user,
                category=category,
                rating=rating,
            )
        overall, _ = OverallStarRating.objects.get_or_create(
            object_id=rating_object.pk, content_type=ct, category=category
        )
        rating_obj.overall_score = overall
        rating_obj.rating = rating
        rating_obj.save()
        overall.update()
        return overall.rating

    class Meta:
        unique_together = [
            ("object_id", "content_type", "voter", "score"),
        ]

    def __str__(self):
        return str(self.score)


class Content(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    text = models.TextField(_("Conetent field"), max_length=500, blank=True)
    overall_star_rating = GenericRelation(OverallStarRating)
    star_rating = GenericRelation(StarRating)
