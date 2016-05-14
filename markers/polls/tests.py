import json

import pytest
from django.core.urlresolvers import resolve
from django.contrib.auth.models import User
from django.core import serializers
from django.test import TestCase
from django.http import HttpRequest

from polls.views import polls, responses, add_response
from polls.models import Topic, Poll, PollChoice, Response

# Create your tests here.
"""
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


class Responses(TestCase):

    def test_can_create_responses(self):
        user=User.objects.create_user('bob', 'orcpass')
        user.save()

        topic=Topic.objects.create()
        poll=Poll.objects.create(name='New State Bird', topic=topic)
        first_poll_choice=PollChoice.objects.create(text='Pidgey', poll=poll)

        response=Response.objects.create(poll_choice=first_poll_choice, user=user)

        all_responses=Response.objects.all()
        first_response=all_responses[0]
        self.assertEqual(first_response.poll_choice.poll.name, 'New State Bird')

    def test_responses_view_returned_by_correct_url(self):
        topic=Topic.objects.create()
        poll=Poll.objects.create(name='New State Bird', topic=topic)
        first_poll_choice=PollChoice.objects.create(text='Pidgey', poll=poll)

        found=resolve('/polls/{0}/'.format(poll.id))
        self.assertEqual(found.func, responses)

    def test_responses_view_returns_all_possible_responses(self):
        bob_user=User.objects.create_user('bob', password='orcpass')
        bob_user.save()

        tom_user=User.objects.create_user('tom', password='tompass')
        tom_user.save()

        topic=Topic.objects.create()
        poll=Poll.objects.create(name='New State Bird', topic=topic)

        first_poll_choice=PollChoice.objects.create(text='Pidgey', poll=poll)
        second_poll_choice=PollChoice.objects.create(text='A Porcupine', poll=poll)

        first_response=Response.objects.create(poll_choice=first_poll_choice, user=bob_user)
        second_response=Response.objects.create(poll_choice=second_poll_choice, user=tom_user)

        request=HttpRequest()
        response=responses(request, poll.id).content

        deserialized_objs = list(serializers.deserialize('json', response))
        self.assertEqual(deserialized_objs[0].object.user.username, 'bob')
        self.assertEqual(deserialized_objs[1].object.poll_choice.poll.name, 'New State Bird')

    def test_add_response_url_returns_correct_view(self):
        topic=Topic.objects.create()
        poll=Poll.objects.create(name='New State Bird', topic=topic)

        found = resolve('/polls/{0}/add/'.format(poll.id))
        self.assertEqual(found.func, add_response)

    def test_can_add_response_via_url(self):
        bob_user=User.objects.create_user('bob', password='orcpass')
        bob_user.save()

        topic=Topic.objects.create()
        poll=Poll.objects.create(name='New State Bird', topic=topic)

        first_poll_choice=PollChoice.objects.create(text='Pidgey', poll=poll)
        second_poll_choice=PollChoice.objects.create(text='A Porcupine', poll=poll)

        self.client.login(username='bob', password='orcpass')
        self.client.post(
                '/polls/{0}/add/'.format(poll.id),
                 data={'poll_choice_id': first_poll_choice.id}
                 )
        self.assertEqual(Response.objects.count(), 1)
        response=Response.objects.first()
        self.assertEqual(response.poll_choice.id, first_poll_choice.id)
        self.assertEqual(response.user.id, bob_user.id)

"""
