from django.contrib import admin

from .models import Content


# class Rate(admin.TabularInline):
#     model = Rating
#     extra = 0


# class ContentAdmin(admin.ModelAdmin):
#     inlines = [Rate, ]


admin.site.register(Content)
