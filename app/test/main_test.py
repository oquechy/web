from fastapi.testclient import TestClient

import numpy as np
import cv2
import os

from ..main import app
from .. import db

from .. import helper

import logging

LOGGER = logging.getLogger(__name__)


def test_root():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    resp = response.json()
    assert len(resp) == 4
    assert "welcome" in resp["description"].lower()
    assert resp["closet_size"] == len(db.closet())
    assert resp["summer_looks"] == db.summer_looks()
    assert resp["winter_looks"] == db.winter_looks()


def test_closet():
    client = TestClient(app)
    response = client.get("/closet")
    assert response.status_code == 200
    image_np = np.frombuffer(response.content, np.uint8)
    got = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    want = cv2.imread(os.path.join("test", "canonic",
                      "closet.jpg"))
    helper.cv2_eq(got, want)


def test_favicon():
    client = TestClient(app)
    response = client.get("/favicon.ico")
    assert response.status_code == 200


def test_randomize_no_field():
    client = TestClient(app)
    response = client.get("/randomize")
    assert response.status_code == 422
    assert "field required" in response.json()["detail"][0]["msg"]


def test_randomize_invalid_field():
    client = TestClient(app)
    response = client.get("/randomize?season=2022")
    assert response.status_code == 422
    assert "value is not a valid enumeration member" in response.json()[
        "detail"][0]["msg"]


def test_randomize_summer():
    client = TestClient(app)
    response = client.get("/randomize?season=summer")
    assert response.status_code == 200

    image_np = np.frombuffer(response.content, np.uint8)
    got = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    helper.cv2_size(got, 2500, 1500)


def test_randomize_winter():
    client = TestClient(app)
    response = client.get("/randomize?season=winter")
    assert response.status_code == 200

    image_np = np.frombuffer(response.content, np.uint8)
    got = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    helper.cv2_size(got, 2500, 2000)


def test_show():
    client = TestClient(app)
    response = client.get("/show/top/2")
    assert response.status_code == 200

    image_np = np.frombuffer(response.content, np.uint8)
    got = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    helper.cv2_eq(got, cv2.imread(os.path.join("images", "top", "3.png")))


def test_show_out_of_bound():
    client = TestClient(app)
    response = client.get("/show/top/200")
    assert response.status_code == 422
    n = len(db.top())
    assert "Expected 0 <= item_id < " + str(n) in response.json()["detail"]


def test_show_no_args():
    client = TestClient(app)
    response = client.get("/show")
    assert response.status_code == 404
    assert "Not Found" in response.json()["detail"]


def test_show_wrong_type():
    client = TestClient(app)
    response = client.get("/show/asseccories/1")
    assert response.status_code == 422
    assert "value is not a valid enumeration member" in response.json()[
        "detail"][0]["msg"]
