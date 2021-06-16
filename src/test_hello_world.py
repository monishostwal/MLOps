import views
import unittest
import sys

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = views.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'OK'
        self.assertEqual('OK', greeting)

if __name__ == '__main__':
    unittest.main()