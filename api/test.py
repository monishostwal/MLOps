import mlApi
import unittest
import requests
import app

class TestHelloWorld(unittest.TestCase):
	def setUp(self):
		self.app = app.app.test_client()
		self.app.testing = True

	def test_greeting_message(self):

	
		self.assertEqual(
		    requests.post('http://127.0.0.1:5000/flowers/predict',json= {
		"feature":[1,2,3,4]}).json(),"virginica")


if __name__ == '__main__':
    unittest.main()




  
