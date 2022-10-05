import unittest
from parameterized import parameterized
from fastapi.testclient import TestClient

import os

from ..closet_server import app

prefix = "out"


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        ["/", "fetch stats"],
        ["/closet", "fetch closet"],
        ["/favicon.ico", "fetch favicon"],
        ["/randomize?season=summer", "randomize outfit"],
        ["/show/top/2", "fetch item"],
    ])
    def test_log(self, req, log):
        TestClient(app).get(req)
        with open(os.path.join(prefix, "log"), "r") as f:
            last_line = f.readlines()[-1]
        self.assertEqual(log + "\n", last_line)
