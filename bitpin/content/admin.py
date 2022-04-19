from django.contrib import admin

from .models import Content, OverallStarRating, StarRating


class Rate(admin.TabularInline):
    model = StarRating
    extra = 0


class ContentAdmin(admin.ModelAdmin):
    inlines = [Rate, ]


# admin.site.register(Content, ContentAdmin)  # TODO :: it didn't work!
admin.site.register(Content)
admin.site.register(OverallStarRating)
admin.site.register(StarRating)
