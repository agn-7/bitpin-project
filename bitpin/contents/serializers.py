from rest_framework import serializers

from .models import Content
from star_ratings.models import Rating, UserRating
from star_ratings.serializers import RatingSerializer, UserRatingSerializer


class ContentSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField()
    rates = RatingSerializer(source="rating")

    def get_user_rate(self, instance):
        user_rating = instance.rating.limited_user
        return user_rating[0].score if len(user_rating) == 1 else None

    class Meta:
        fields = "__all__"
        model = Content
