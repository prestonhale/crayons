import json
from django.core.urlresolvers import resolve
from django.core import serializers
from django.test import TestCase
from django.http import HttpRequest
from polls.views import polls
from polls.models import Topic, Poll

# Create your tests here.

class HomePage(TestCase):

	def test_open_polls_url_returns_polls_view(self):
		found = resolve('/polls/')
		self.assertEqual(found.func, polls)


	def test_saving_and_retrieving_polls(self):
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

		all_polls=Poll.objects.all()
		first_saved_item=all_polls[0]
		second_saved_item=all_polls[1]

		self.assertEqual(first_saved_item.name, "New State Bird")
		self.assertEqual(second_saved_item.name, "Death Penalty for Badgers?")


	def test_polls_view_returns_all_polls(self):
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

		request=HttpRequest()
		response=polls(request).content
		deserialized_objs = list(serializers.deserialize('json', response))
		self.assertEqual(deserialized_objs[0].object.name, 'New State Bird')
		self.assertEqual(deserialized_objs[1].object.name, 'Death Penalty for Badgers?')


	def test_responses_view_returns_all_possible_responses(self):
		pass
