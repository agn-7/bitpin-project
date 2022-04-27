import pytest

# from hypothesis.extra.django import TestCase

from contents.models import Content
from star_ratings.models import UserRating, Rating
from users.models import CustomUser


@pytest.mark.django_db
def test_create_content():
    content = Content.objects.create(title="Test", text="Something else.")
    assert content.title == "Test"
    assert content.text == "Something else."
    assert Content.objects.filter(title="Test", text="Something else.").exists()

    user = CustomUser.objects.create(username="admin", password="admin")
    rating = Rating.objects.create(count=0, average=0, content=content)
    user_rating = UserRating.objects.create(user=user, score=5, rating=rating)

    assert rating.count == 1
    assert rating.average == 5
    assert Rating.objects.filter(count=1, average=5, content=content).exists()
