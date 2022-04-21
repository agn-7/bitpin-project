from rest_framework import serializers

from .models import Rating, UserRating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('count', 'average')
        model = Rating
