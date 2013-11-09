from unittest import TestCase

from installer import web


class WebTest(TestCase):
    def test_index(self):
        app = web.app.test_client()
        response = app.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual("ok", response.data)
