import os
import sys
import pytest

from rest_framework.test import APIClient
from django.test import Client

from colored_print import ColoredPrint


log = ColoredPrint()
sys.path.append(os.path.dirname(__file__))
TOKEN_URL = "/api-token-auth/"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def token(api_client):
    payload = dict(username="admin", password="admin")  # They come from setup() in e2e
    response = api_client.post(
        TOKEN_URL,
        payload,
    )
    log.success(f"status: {response.status_code}")
    token = response.json()["token"]
    log.success(token)
    return token


@pytest.fixture
def header(token):
    header = {"Authorization": "Token {}".format(token)}
    log.success(header)
    return header


@pytest.fixture
def auth_api_client(api_client, token):
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token)
    return api_client


@pytest.fixture
def auth_client(token):
    client = Client(HTTP_AUTHORIZATION="Token " + token)
    return client
