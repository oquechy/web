from fastapi.testclient import TestClient

import random


from .main import app
from . import db


import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.integration_test
def test_show_all():
    client = TestClient(app)

    response = client.get("/")
    assert response.status_code == 200, response.json()

    for t, items in [
        ("top", db.top()),
        ("bottom", db.bottom()),
        ("shoes", db.shoes()),
        ("hats", db.hats()),
        ("bags", db.bags()),
        ("outwear", db.outwear()),
        ("accessories", db.accessories()),
    ]:
        for id in range(len(items)):
            response = client.get("/show/" + t + "/" + str(id))
            assert response.status_code == 200, response.json()

    response = client.get("/show/" + t + "/" + str(len(items)))
    assert response.status_code == 422, response.json()


@pytest.mark.slow_integration_test
def test_randomize_loop():
    client = TestClient(app)

    response = client.get("/closet")
    assert response.status_code == 200, response.json()

    for _ in range(40):
        response = client.get("/randomize?season=summer")
        assert response.status_code == 200, response.json()

        response = client.get("/randomize?season=winter")
        assert response.status_code == 200, response.json()

        response = client.get("/randomize?season=2022")
        assert response.status_code == 422, response.json()
        response = client.get("/randomize")
        assert response.status_code == 422, response.json()


@pytest.mark.slow_integration_test
def test_random_queries():
    client = TestClient(app)

    qs = [
        ("/", 200),
        ("/favicon.ico", 200),
        ("/closet", 200),
        ("/show/top/1", 200),
        ("/show/bags/2", 200),
        ("/show/accessories/3", 200),
        ("/randomize?season=summer", 200),
        ("/randomize?season=winter", 200),

        ("/nonono", 404),
        ("/randomize?season=2022", 422),
        ("/randomize", 422),
        ("/randomize/2", 404),
        ("/show", 404),
        ("/show/nonono", 404),
        ("/show/top/nonono", 422),
        ("/show/bags/2000", 422),
        ("/show/accessories/", 404),
    ]

    for (q, r) in random.choices(qs, k=100):
        response = client.get(q)
        assert response.status_code == r, q
