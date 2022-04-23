from django.contrib import admin

from star_ratings.models import UserRating, Rating
from .models import Content


# class RatingAdmin(admin.TabularInline):
#     def get_queryset(self, request):
#         return super(RatingAdmin, self).get_queryset(request).select_related('rating', 'user').prefetch_related('rating__content')
#     model = Rating
#     extra = 0


# class ContentAdmin(admin.ModelAdmin):
#     inlines = [RatingAdmin, ]


admin.site.register(Content)
