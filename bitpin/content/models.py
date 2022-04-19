from django.db import models
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


class Content(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    text = models.TextField(_("Conetent field"), max_length=500, blank=True)
