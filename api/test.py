import mlApi
import unittest
import requests

class TestHelloWorld(unittest.TestCase):

    def test_greeting_message(self):

        headers = {'Content-Type': 'application/json'}

        self.assertEqual(
            requests.post('http://127.0.0.1:5000/flowers/predict',json= {
    "feature":[1,2,3,4]}).json(),"virginica")


if __name__ == '__main__':
    unittest.main()