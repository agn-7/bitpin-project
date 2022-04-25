from django.db import models
from django.utils.translation import gettext_lazy as _


class Content(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    text = models.TextField(_("Content field"), max_length=500, blank=True)
