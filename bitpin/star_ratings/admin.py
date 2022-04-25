from __future__ import unicode_literals

from django.contrib import admin

from .models import UserRating, Rating


class UserRatingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "score")


class RatingAdmin(admin.ModelAdmin):
    list_display = ("__str__", "average", "count")


admin.site.register(Rating, RatingAdmin)
admin.site.register(UserRating, UserRatingAdmin)
