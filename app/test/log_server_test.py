import unittest
from parameterized import parameterized
from fastapi.testclient import TestClient

import os

from ..closet_server import app

prefix = "out"


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["/", "INFO fetch stats"],
        ["/closet", "INFO fetch closet"],
        ["/favicon.ico", "INFO fetch favicon"],
        ["/randomize?season=summer", "INFO randomize outfit"],
        ["/show/top/2", "INFO fetch item"],
        ["/show/top/200", "ERRO Expected 0 <= item_id <= 6, got: 200"],
        ["/show/bottom/300", "ERRO Expected 0 <= item_id <= 3, got: 300"],
    ])
    def test_log(self, req, log):
        TestClient(app).get(req)
        with open(os.path.join(prefix, "log"), "r") as f:
            last_line = f.readlines()[-1]
        self.assertEqual(log + "\n", last_line)
