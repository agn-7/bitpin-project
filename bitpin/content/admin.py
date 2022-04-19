from django.contrib import admin

from pinax.ratings.models import OverallRating, Rating

from .models import Content


class Rate(admin.TabularInline):
    model = Rating
    extra = 0


class ContentAdmin(admin.ModelAdmin):
    inlines = [Rate, ]


# admin.site.register(Content, ContentAdmin)  # TODO :: it didn't work!
admin.site.register(Content)
admin.site.register(OverallRating)
admin.site.register(Rating)
