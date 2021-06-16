import hello_world
import unittest
import requests
class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = hello_world.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/flowers/predict',json= {
"feature":[1,2,3,4]})

        self.assertEqual(response.json, 'virginica')
    
    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD'
        self.assertEqual(hello_world.greet(), greeting)

    def test_model_predictions(self):
        self.assertEqual(hello_world.test_model_output(),"virginica")

if __name__ == '__main__':
    unittest.main()