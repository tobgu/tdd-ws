import unittest
from nose.plugins.attrib import attr
from webapp import app


class TestWebApp(unittest.TestCase):

    def test_it_can_serve_HTTP(self):
        browser = app.test_client()
        response = browser.get('/')

        self.assertEqual(response.status_code, 200)

