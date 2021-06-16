import hello_world
import unittest
import requests
class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(hello_world.greet(), greeting)

    def test_model_predictions(self):
        self.assertEqual(
 requests.get('http://127.0.0.1:5000/flowers/predict',json= {
"feature":[1,2,3,4]}).json(),"virginica")

if __name__ == '__main__':
    unittest.main()