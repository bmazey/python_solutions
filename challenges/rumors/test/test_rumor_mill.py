from unittest import TestCase
from challenges.rumors.src.application import create_app

# adding comments for travis CI


class SomeTest(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get('/api/rumor/')
        self.assertTrue(200, response.status_code)
