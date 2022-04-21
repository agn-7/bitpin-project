from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .models import UserRating, Rating
from django.utils.html import format_html


class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'score')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'average', 'count')


admin.site.register(Rating, RatingAdmin)
admin.site.register(UserRating, UserRatingAdmin)
