from django.test import TestCase
from voters.views import create_voter
from voters.models import Voter, CellCarrier
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User


# Create your tests here.
class Voters(TestCase):

	def test_create_voter_url_returns_correct_view(self):
		response=resolve('/voters/create/')
		self.assertEqual(response.func, create_voter)

	def test_create_voter_post_creates_user(self):
		carrier = CellCarrier.objects.create(name="T-Mobile", sms_gateway="@tmomail.net")
		self.client.post(
			'/voters/create/',
			data={
				'username': 'TestUser',
				'password': 'password',
				'phone': '904-400-3999',
				'carrier': carrier.id,
				})
		user=User.objects.first()
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(user.username, 'TestUser')

	def test_create_voter_creates_voter_model(self):
		carrier = CellCarrier.objects.create(name="T-Mobile", sms_gateway="@tmomail.net")
		self.client.post(
			'/voters/create/',
			data={
				'username': 'TestUser',
				'password': 'password',
				'email': 'slethik@gmail.com',
				'phone': '904-400-3999',
				'carrier': carrier.id,
			})
		voter=Voter.objects.first()
		self.assertEqual(Voter.objects.count(), 1)
		self.assertEqual(voter.phone, '904-400-3999')

	def test_text_sent_from_validate_phone_url(self):
		user=User.objects.create(username='bob', password='orcington')
		carrier = CellCarrier.objects.create(name="T-Mobile", sms_gateway="@tmomail.net")
		Voter.objects.create(user=user, phone='9044003999', carrier=carrier)

		self.client.post(
			'/voters/validate-phone/', data={'user_id': user.id})
