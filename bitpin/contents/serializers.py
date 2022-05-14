from rest_framework import serializers

from .models import Content
from star_ratings.models import Rating, UserRating
from star_ratings.serializers import RatingSerializer, UserRatingSerializer


class ContentSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField()
    rates = RatingSerializer(source="rating")

    def get_user_rate(self, instance):
        user_id = self.context.get("user_id")
        user_rating = instance.rating.user_ratings.filter(user=user_id)
        serializer = UserRatingSerializer(
            instance=user_rating, many=True, read_only=True
        )
        return serializer.data

    class Meta:
        fields = "__all__"
        model = Content
