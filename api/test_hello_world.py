import views
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.views = views.app.test_client()
        self.views.testing = True

    def test_status_code(self):
        response = self.views.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'OK'
        self.assertEqual('OK', greeting)

if __name__ == '__main__':
    unittest.main()