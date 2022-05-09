import pytest

from model_bakery import baker
from unittest.mock import patch

from star_ratings.models import UserRating, Rating
from contents.models import Content
from users.models import CustomUser
from contents.views import ContentView
from star_ratings.views import RatingView

pytestmark = pytest.mark.django_db


class TestEndpoints:
    content_endpoint = "/api/v1/content/"
    rate_endpoint = "/api/v1/rate/"
    token_url = "/api-token-auth/"

    def setup(self) -> None:
        self.user = baker.make(CustomUser, _quantity=2)
        self.content = baker.make(Content)
        # self.content = baker.prepare(Content)
        # self.content.save()
        self.rating = baker.make(Rating, content=self.content)
        UserRating.objects.create(user=self.user[0], score=5, rating=self.rating)
        UserRating.objects.create(score=1, rating=self.rating)
        usr = CustomUser.objects.create(username="admin", password="admin")
        usr.set_password(usr.password)
        usr.save()

    @patch.object(ContentView, "permission_classes", [])
    def test_get_cotent(self, api_client):
        assert Rating.objects.filter(
            count=self.rating.count, average=self.rating.average, content=self.content
        ).exists()

        response = api_client.get(
            self.content_endpoint,
        )

        print(response.data)
        assert response.status_code == 200
        data = response.json()[0]
        assert data["title"] == self.content.title
        assert float(data["rate"][0]["average"]) == self.rating.average

    @patch.object(RatingView, "permission_classes", [])
    def test_post_rate(self, api_client):
        payload = dict(content_id=self.content.id, score=5)
        response = api_client.post(
            self.rate_endpoint,
            payload,
        )
        print(response.data)
        assert response.status_code in (201, 200)

        wrong_payload = dict(content_id=self.content.id + 10, score=5)
        response = api_client.post(
            self.rate_endpoint,
            wrong_payload,
        )
        assert response.status_code == 400
