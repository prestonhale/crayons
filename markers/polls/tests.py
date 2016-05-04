from django.core.urlresolvers import resolve
from django.test import TestCase
from polls.views import polls

# Create your tests here.

class HomePage(TestCase):

	def test_open_polls_url_returns_polls_view(self):
		found = resolve('/polls/')
		self.assertEqual(found.func, polls)