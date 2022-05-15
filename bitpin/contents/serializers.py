from rest_framework import serializers

from .models import Content
from star_ratings.models import Rating, UserRating
from star_ratings.serializers import RatingSerializer, UserRatingSerializer


class ContentSerializer(serializers.ModelSerializer):
    user_rate = serializers.SerializerMethodField()
    rates = RatingSerializer(source="rating")

    def get_user_rate(self, instance):
        user_id = self.context.get("user_id")
        user_rating = instance.rating.user_ratings.all()

        """
        It reduces the number of query, however in the case of the huge amount of
        the user_rating is a bottle neck!
        """
        for u in user_rating:
            if u.user_id == user_id:
                return u.score
        return None

        # user_rating = instance.rating.user_ratings.filter(user=user_id)  # increases the number of queries
        # serializer = UserRatingSerializer(  # TODO
        #     instance=user_rating, many=True, read_only=True
        # )
        # return serializer.data

    class Meta:
        fields = "__all__"
        model = Content
