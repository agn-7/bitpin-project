from rest_framework import serializers

from .models import Content
from star_ratings.models import Rating, UserRating
from star_ratings.serializers import RatingSerializer, UserRatingSerializer


class ContentSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()
    user_rate = serializers.SerializerMethodField()

    def get_rate(self, instance):
        self.rating = Rating.objects.filter(content=instance)
        serializer = RatingSerializer(instance=self.rating, many=True, read_only=True)
        return serializer.data

    def get_user_rate(self, instance):
        user_id = self.context.get("user_id")
        user_rating = UserRating.objects.filter(rating=self.rating[0], user=user_id)
        serializer = UserRatingSerializer(
            instance=user_rating, many=True, read_only=True
        )
        return serializer.data

    class Meta:
        fields = "__all__"
        model = Content
