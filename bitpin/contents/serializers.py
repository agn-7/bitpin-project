from rest_framework import serializers

from .models import Content
from star_ratings.models import Rating
from star_ratings.serializers import RatingSerializer


class ContentSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Content

    def get_rate(self, instance):
        rating_models = Rating.objects.filter(content=instance)
        serializer = RatingSerializer(instance=rating_models,
                                    many=True, read_only=True)
        return serializer.data
