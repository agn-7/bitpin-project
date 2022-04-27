import pytest

# from hypothesis.extra.django import TestCase

from contents.models import Content


@pytest.mark.django_db
def test_create_category():
    content = Content.objects.create(title="Test", text="Something else.")
    assert content.title == "Test"
    assert content.text == "Something else."
    assert Content.objects.filter(title="Test", text="Something else.").exists()
