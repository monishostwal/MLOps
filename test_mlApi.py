import mlApi
import unittest
import requests


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = mlApi.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/flowers/predict', json={
            "feature": [1, 2, 3, 4]})

        self.assertEqual(response.json, 'virginica')


if __name__ == '__main__':
    unittest.main()
