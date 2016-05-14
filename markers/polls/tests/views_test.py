import json

import pytest
from django.core.urlresolvers import resolve, reverse
from django.contrib.auth.models import User
from django.test import TestCase

from polls.views import polls, responses, add_response
from polls.models import Topic, Poll, PollChoice, Response

# Create your tests here.

def test_open_polls_url_returns_polls_view():
    found = resolve('/polls/')
    assert found.func == polls

def test_poll_endpoint(client, sample_poll):
    poll1 = sample_poll()
    poll2 = sample_poll()
    path = reverse('polls')
    response = client.get(path)
    data = response.json()["data"]
    assert len(data) == 2


"""
class Responses(TestCase):

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

