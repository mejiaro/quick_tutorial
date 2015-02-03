import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
	"""docstring for TutorialViewTests"""
	def setUp(self):
		self.config = testing.setUp()

	def tearDown(self):
		testing.tearDown()

	def test_hello_world(self):
		from tutorial import hello_world

		request = testing.DummyRequest()
		response = hello_world(request)
		self.assertIn("Hello World!", response.body)
		self.assertEqual(response.status_code, 200)

class TutorialFunctionalTests(unittest.TestCase):
	"""docstring for TutorialFunctionalTests"""
	def setUp(self):
		from tutorial import main
		app = main({})
		from webtest import TestApp

		self.testapp = TestApp(app)

	def test_hello_world(self):
		res = self.testapp.get('/', status=200)
		self.assertIn('<h1>Hello World!</h1>', res.body)