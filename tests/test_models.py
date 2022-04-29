from django.forms import ValidationError
import pytest

# from hypothesis.extra.django import TestCase

from contents.models import Content
from star_ratings.models import UserRating, Rating
from users.models import CustomUser


@pytest.mark.django_db
def test_models():
    content = Content.objects.create(title="Test", text="Something else.")
    assert content.title == "Test"
    assert content.text == "Something else."
    assert Content.objects.filter(title="Test", text="Something else.").exists()

    user = CustomUser.objects.create(username="admin", password="admin")
    rating = Rating.objects.create(count=0, average=0, content=content)
    UserRating.objects.create(user=user, score=5, rating=rating)
    UserRating.objects.create(score=1, rating=rating)
    assert rating.count == 2
    assert rating.average == 3
    assert Rating.objects.filter(count=2, average=3, content=content).exists()

    with pytest.raises(ValidationError):
        UserRating.objects.create(score=6, rating=rating)
    