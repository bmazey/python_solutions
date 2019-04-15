from unittest import TestCase
from challenges.rumors.src.application import get_app

# adding comments for travis CI


class RumorMillTest(TestCase):
    def setUp(self):
        self.application = get_app()
        self.client = self.application.test_client()

    def test_simple_get(self):
        response = self.client.get('/rumor')
        print(response.get_json())
        self.assertTrue(200, response.status_code)
        self.assertTrue(response.get_json().get('brandon') == 'listens to selena gomez')

    # def test_post_and_get(self):
    #     response = self.client.post('/rumor', data=dict(name='alyssa', content='cheated on her spanish homework'))
    #     print(response.json())
    #     self.assertTrue(200, response.status_code)
    #     # self.assertTrue(response.get_json().get('brandon') == 'listens to selena gomez')


