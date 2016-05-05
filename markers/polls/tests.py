import json
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.core import serializers
from django.test import TestCase
from django.http import HttpRequest
from polls.views import polls, responses
from polls.models import Topic, Poll, PollChoice, Response

# Create your tests here.

class HomePage(TestCase):

	def helper_set_up_sample_polls(self):
		topic=Topic()
		topic.save()

		first_poll=Poll()
		first_poll.name="New State Bird"
		first_poll.topic=topic
		first_poll.save()

		second_poll=Poll()
		second_poll.name="Death Penalty for Badgers?"
		second_poll.topic=topic
		second_poll.save()


	def test_open_polls_url_returns_polls_view(self):
		found = resolve('/polls/')
		self.assertEqual(found.func, polls)


	def test_saving_and_retrieving_polls(self):
		self.helper_set_up_sample_polls()

		all_polls=Poll.objects.all()
		first_saved_item=all_polls[0]
		second_saved_item=all_polls[1]

		self.assertEqual(first_saved_item.name, "New State Bird")
		self.assertEqual(second_saved_item.name, "Death Penalty for Badgers?")


	def test_polls_view_returns_all_polls(self):
		self.helper_set_up_sample_polls()

		request=HttpRequest()
		response=polls(request).content
		deserialized_objs = list(serializers.deserialize('json', response))
		self.assertEqual(deserialized_objs[0].object.name, 'New State Bird')
		self.assertEqual(deserialized_objs[1].object.name, 'Death Penalty for Badgers?')


	def test_can_create_user(self):
		user=User.objects.create_user('bob', 'orcpass')
		user.save()

		self.assertEqual(User.objects.all()[0].username, 'bob')


	def test_can_create_responses(self):
		user=User.objects.create_user('bob', 'orcpass')
		user.save()

		topic=Topic()
		topic.save()

		poll=Poll()
		poll.name="New State Bird"
		poll.topic=topic
		poll.save()

		first_poll_choice=PollChoice()
		first_poll_choice.name="Pidgey"
		first_poll_choice.poll=poll
		first_poll_choice.save()

		response=Response()
		response.poll_choice=first_poll_choice
		response.user=user
		response.save()

		all_responses=Response.objects.all()
		first_response=all_responses[0]
		self.assertEqual(first_response.poll_choice.poll.name, 'New State Bird')


	def test_responses_view_returns_all_possible_responses(self):
		bob_user=User.objects.create_user('bob', 'orcpass')
		bob_user.save()

		tom_user=User.objects.create_user('tom', 'tompass')
		tom_user.save()

		topic=Topic()
		topic.save()

		poll=Poll()
		poll.name="New State Bird"
		poll.topic=topic
		poll.save()

		first_poll_choice=PollChoice()
		first_poll_choice.name="Pidgey"
		first_poll_choice.poll=poll
		first_poll_choice.save()

		second_poll_choice=PollChoice()
		second_poll_choice.name="A Porcupine"
		second_poll_choice.poll=poll
		second_poll_choice.save()

		first_response=Response(poll_choice=first_poll_choice, user=bob_user)
		first_response.save()

		second_response=Response(poll_choice=second_poll_choice, user=tom_user)
		second_response.save()

		request=HttpRequest()
		response=responses(request, poll.id).content

		deserialized_objs = list(serializers.deserialize('json', response))
		self.assertEqual(deserialized_objs[0].object.user.username, 'bob')
		self.assertEqual(deserialized_objs[1].object.poll_choice.poll.name, 'New State Bird')

